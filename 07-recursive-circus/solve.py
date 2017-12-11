import fileinput
import re
from functools import lru_cache

nodes = {}

@lru_cache()
def weight(nodeId):
    return nodes[nodeId]['weight'] + sum(weight(child) for child in nodes[nodeId]['children'])

def is_balanced(nodeId):
    if len(nodes[nodeId]['children']) < 3:
        return True
    child_weights = [weight(child) for child in nodes[nodeId]['children']]

    first = child_weights[0]
    return all(first == w for w in child_weights)

def main():
    regex = re.compile(r'^(?P<id>[a-z]+) \((?P<weight>[0-9]+)\)( -> (?P<children>.*))?$')
    for line in fileinput.input():
        line = line.strip()
        matches = regex.match(line).groupdict()
        matches["children"] = set(re.split(r"[, ]+", matches["children"])) if matches["children"] else []
        matches['weight'] = int(matches['weight'])
        nodes[matches["id"]] = matches

    (root,) = nodes.keys() - set().union(*(node['children'] for node in nodes.values()))
    print(root)

    sorted_nodes = sorted((n for n in nodes.values() if not is_balanced(n['id'])), reverse=True, key=lambda n: weight(n['id']))
    print(list(weight(id) for id in list(sorted_nodes)[0]['children']))
if __name__ == "__main__":
    main()