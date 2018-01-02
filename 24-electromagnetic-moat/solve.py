import fileinput

components = set(tuple(map(int, l.strip().split('/'))) for l in fileinput.input())

def other(component, connector):
    return component[1] if component[0] == connector else component[0]

def solve1(components, used, current_connector):
    remaining = components - used
    compatible = filter(lambda c: current_connector in c, remaining)
    values = (sum(c) + solve1(components, used | {c}, other(c, current_connector)) for c in compatible)
    return max(values, default=0)


def solve2(components, used, current_connector):
    remaining = components - used
    compatible = filter(lambda c: current_connector in c, remaining)
    values = (100000 + sum(c) + solve2(components, used | {c}, other(c, current_connector)) for c in compatible)
    return max(values, default=0)


print(solve1(components, set(), 0))
print(solve2(components, set(), 0))

