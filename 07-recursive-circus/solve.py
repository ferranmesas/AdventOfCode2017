import fileinput
import re
from functools import lru_cache

nodes = {}

@lru_cache()
def weight(nodeId):
    node = nodes[nodeId]
    if "childs_weight" not in node:
        node["childs_weight"] = sum(weight(child) for child in node['children'])
    return node['weight'] + node["childs_weight"]

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
    map(weight, nodes.keys())

    unbalanced_nodes = [n for n in nodes.values() if not is_balanced(n['id'])]
    print(unbalanced_nodes)
    for node in ['utnrb', 'bbytzn', 'fzvctf']:
        print(node, weight(node))
if __name__ == "__main__":
    main()