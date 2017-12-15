import re
import fileinput

stack = 0
total = 0

ignore = re.compile(r'!.')
garbage = re.compile(r'<.*?>')

line = next(iter(fileinput.input())).strip()


print(line)
line = re.sub(ignore, "", line)
print(line)
garbages = re.findall(garbage, line)

print(sum(len(g) - 2 for g in garbages))