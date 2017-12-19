from collections import Counter

input = "amgozmfv"

def reverse_range(list, frm, amt):
    for i in range(amt // 2):
        idx1 = (frm + i) % len(list)
        idx2 = (frm + amt - i - 1) % len(list)
        list[idx1], list[idx2] = list[idx2], list[idx1]

def knot_hash(message):
    digested = [ord(x) for x in message] + [17, 31, 73, 47, 23]
    l = 256
    rope = list(range(l))
    pos = 0
    skip = 0
    for _ in range(64):
        for i in digested:
            reverse_range(rope, pos, i)
            pos = (pos + i + skip) % l
            skip = (skip + 1) % l
    
    hash_result = []
    for i in range(0, 256, 16):
        section = rope[i:i+16]
        total = 0
        for number in section:
            total ^= number
        hash_result.append(format(total, '02x'))
    return(''.join(hash_result))

dirs = [
[-1, 0],
[0, 1],
[1, 0],
[0, -1],
]
def p(m):
    print('\n'.join(''.join(map(str, r)) for r in m))

def find_adjacent_groups(matrix):
    total = 0
    for idx, row in enumerate(matrix):
        for idy, cell in enumerate(row):
            if cell == 1:
                total += 1
                open = set()
                open.add((idx, idy))
                while True:
                    if not open:
                        break
                    currx, curry = open.pop()
                    matrix[currx][curry] = chr((total % 26) + ord('a'))
                    for dx, dy in dirs:
                        ddx, ddy = currx + dx, curry + dy
                        if ddx >= 0 and ddx < len(matrix) and ddy >= 0 and ddy < len(row) and matrix[ddx][ddy] == 1:
                            open.add((ddx, ddy))
    return total


def part1():
    total = Counter()
    for i in range(128):
        m = input + "-" + str(i)
        h = knot_hash(m)
        b = format(int(h, 16), "0128b")
        total.update(b)
    print(total['1'])

def part2():
    memory = []
    for i in range(128):
        m = input + "-" + str(i)
        h = knot_hash(m)
        b = format(int(h, 16), "0128b")
        memory.append([int(x) for x in b])
    #memory = [r[:8] for r in memory][:8]
    print(find_adjacent_groups(memory))

part2()




