import fileinput
import re

def state(line):
    return re.search(r'state ([A-Z])', line).group(1)

def steps(line):
    return int(re.search(r'([0-9]+) steps', line).group(1))

def value(line):
    return int(re.search(r'value (?:is )?([0-9]+)', line).group(1))

def move(line):
    return re.search(r'to the (right|left)', line).group(1)

def parse(inp):
    initial_state = state(next(inp).strip())
    iters = steps(next(inp).strip())
    next(inp)
    machine = {}

    try:
        while inp:
            s = state(next(inp).strip())
            while True:
                try:
                    v = value(next(inp).strip())
                except:
                    break
                nv = value(next(inp).strip())
                m = move(next(inp).strip())
                ns = state(next(inp).strip())
                machine[(s, v)] = (nv, m, ns)
    except:
        pass

    return initial_state, iters, machine

def main():
    inp = iter(fileinput.input())
    initial_state, iters, machine = parse(inp)
    print(initial_state, iters, machine)

    tape = []
    position = 0
    state = initial_state
    for _ in range(iters):
        if position == -1:
            position = 0
            tape.insert(0, 0)
        elif position >= len(tape):
            tape.append(0)

        v = tape[position]
        nv, m, state = machine[(state, v)]
        tape[position] = nv
        position += 1 if m == 'right' else -1
    print(sum(tape))

if __name__ == '__main__':
    main()
