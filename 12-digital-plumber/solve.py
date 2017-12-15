from collections import defaultdict
import fileinput
import re


graph = defaultdict(set)
for line in fileinput.input():
    [node, _, *connections] =re.split(r'[, ]+', line.strip())
    print(node, connections)
    graph[node].update(connections)
    for c in connections:
        graph[c].add(node)


groups = 0
while graph:
    open = set()
    closed = set()
    open.add(next(iter(graph.keys())))
    while open:
        elem = next(iter(open))
        open.remove(elem)
        for c in graph[elem]:
            if c not in closed:
                open.add(c)
        closed.add(elem)
    for node in closed:
        del graph[node]
    groups += 1

print(groups)