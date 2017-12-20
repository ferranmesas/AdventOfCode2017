from itertools import repeat
import fileinput
programs = [chr(x + ord('a')) for x in range(16)]
orig = programs[:]
def parse(move):
	type, args = move[0], move[1:]
	if type == 's':
		return (type, int(args))
	elif type == 'x':
		return (type, tuple(map(int, args.split('/'))))
	else:
		return (type, tuple(args.split('/')))

moves = list(map(parse, next(iter(fileinput.input())).strip().split(',')))
iters = 0
while True:
	iters += 1
	for type, args in moves:
		if type == 's':
			programs = programs[-args:] + programs[:-args]
		elif type == 'x':
			x, y = args
			programs[x], programs[y] = programs[y], programs[x]
		else:
			a, b = args
			x, y = programs.index(a), programs.index(b)
			programs[x], programs[y] = b, a
	print(orig)
	print(iters, ''.join(programs))
	if programs == orig:
		print(iters)
		break

print(''.join(programs))