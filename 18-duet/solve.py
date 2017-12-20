from __future__ import print_function
from collections import defaultdict
import fileinput




def parse(line):
    cmd = line.strip().split()
    return (cmd[0], cmd[1:])

program = [parse(line) for line in fileinput.input()]

def val(r, x):
    try:
        return int(x)
    except ValueError:
        return r[x]

def other(id):
    return (id+1) % 2

def parallel_runner(pa, pb):
    ps = [pa, pb]
    queues = [[], []]
    sent = [0, 0]
    curr = 0

    second_started = False
    cmd, arg = ps[curr].next()
    while True:
        if cmd == 'snd':
            print('program', curr, 'sends value', arg)
            sent[curr] += 1
            queues[curr].append(arg)
            cmd, arg = ps[curr].next()
            continue
        elif cmd == 'rcv':
            print('program', curr, 'calls rcv')
            if queues[other(curr)]:
                print('and we have something for him:', queues[other(curr)][0])
                cmd, arg = ps[curr].send(queues[other(curr)].pop(0))
                continue
            else:
                print('and we have nothing for him. lets check the other program...')
                if not second_started:
                    print('starting the second program, as it has not been ran yet')
                    second_started = True
                    curr = other(curr)
                    cmd, arg = ps[curr].next()
                    continue
                elif queues[curr]:
                    print('we have something for the other program indeed.')
                    curr = other(curr)
                    cmd, arg = ps[curr].send(queues[other(curr)].pop(0))
                    continue
                else:
                    print("deadlock!", sent)
                    break

def run(program, id):
    pc = 0
    registers = defaultdict(int)
    registers['p'] = id
    while True:
        j = 1
        cmd, args = program[pc]
        if cmd == 'set':
            a, b = args
            registers[a] = val(registers, b)
        elif cmd == 'add':
            a, b = args
            registers[a] += val(registers, b)
        elif cmd == 'mul':
            a, b = args
            registers[a] *= val(registers, b)
        elif cmd == 'mod':
            a, b = args
            registers[a] %= val(registers, b)
        elif cmd == 'snd':
            a, = args
            yield cmd, val(registers, a)
        elif cmd == 'rcv':
            a, = args
            registers[a] = yield cmd, None
        elif cmd == 'jgz':
            a, b = args
            if val(registers, a) > 0:
                j = val(registers, b)
        pc += j


pa = run(program, 0)
pb = run(program, 1)

parallel_runner(pa, pb)
