import fileinput
import re


def reverse_range(list, frm, amt):
    for i in range(amt // 2):
        idx1 = (frm + i) % len(list)
        idx2 = (frm + amt - i - 1) % len(list)
        list[idx1], list[idx2] = list[idx2], list[idx1]

def knot_hash(message, rounds):
    l = 256
    rope = list(range(l))

    pos = 0
    skip = 0
    for _ in range(rounds):
        for i in message:
            reverse_range(rope, pos, i)
            pos = (pos + i + skip) % l
            skip = (skip + 1) % l
    return rope


def part1(inp):
    message = list(map(int, re.split(r'[ ,]', inp)))
    m = knot_hash(message, 1)
    print(m[0] * m[1])

def part2(inp):
    message = list(map(ord, inp)) + [17, 31, 73, 47, 23]
    print(message)
    m = knot_hash(message, rounds=64)
    hash_result = []
    for i in range(0, 256, 16):
        mm = m[i:i+16]
        total = 0
        for number in mm:
            total ^= number
        hash_result.append(format(total, '02x'))
    return(''.join(hash_result))

if __name__ == "__main__":
    inp = next(iter(fileinput.input()))
    print(part2(inp))