import re
import fileinput

stack = 0
total = 0

ignore = re.compile(r'!.')
garbage = re.compile(r'<.*?>')

line = next(iter(fileinput.input())).strip()

print(line)
line = re.sub(",", "", line)
print(line)
line = re.sub(ignore, "", line)
print(line)
line = re.sub(garbage, "", line)
print(line)

for char in line:
    if char == "{":
        stack += 1
    elif char == "}":
        total += stack
        stack -= 1
    else:
        print(char)
        print("woot")

print(total)