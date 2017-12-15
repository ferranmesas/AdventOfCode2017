import fileinput
import operator

moves = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0)
}

if __name__ == "__main__":
    inp = next(iter(fileinput.input())).strip().split(',')
    position = (0, 0, 0)
    m = 0
    for move in inp:
        position = tuple(position[i] + moves[move][i] for i in range(3))
        print(position)
        if max(map(abs, position)) > m:
            m = max(map(abs, position))
    print(max(map(abs, position)))
    print(m)