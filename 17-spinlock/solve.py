from __future__ import print_function
input = 304
result = 0
pos = 0
for i in range(1,50000001):
    pos = (pos + input + 1) % i
    if pos == 0:
        result = i

print(result)
