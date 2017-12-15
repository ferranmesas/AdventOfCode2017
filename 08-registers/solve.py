from collections import defaultdict
import re
import fileinput
import operator

registers = defaultdict(int)

comparison_operators = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}

m = 0
for line in fileinput.input():
    [register, op, amt, _, register_comp, comp, comp_value] = line.strip().split()

    if comparison_operators[comp](registers[register_comp], int(comp_value)):
        registers[register] += (1 if op == "inc" else -1) * int(amt)
    if max(registers.values()) > m:
        m = max(registers.values())
print(max(registers.values()))
print(m)