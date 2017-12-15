import re
import fileinput

firewalls = []
for line in fileinput.input():
    [l, r] = map(int, line.strip().split(': '))
    firewalls.append((l, r))

total = 0
for offset in range(10000000):
    for l, r in firewalls:
        if (offset + l) % ((2 * r) - 2) == 0:
            break
    else:
        print(offset)
        break

