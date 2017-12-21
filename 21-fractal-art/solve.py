import numpy as np
import fileinput

def print_matrix(m):
	for row in m:
		print(''.join('#'if c else '.' for c in row))

def to_array(part):
	return np.array([[ch == '#' for ch in p] for p in part.split('/')], np.bool)

def to_tuple(part):
	return tuple(part.flatten().tolist())

def sections(state):
	size = 3
	if len(state) % 2 == 0:
		size = 2
	secs = len(state) // size
	result = [[None] * secs for _ in range(secs)]
	for i in range(0, len(state), size):
		for j in range(0, len(state), size):
			result[i // size][j // size] = state[i:i+size, j:j+size]
	return result

def find_next_state(state):
	secs = sections(state)
	result = [[None] * len(secs) for _ in range(len(secs))]
	for ix, row in enumerate(secs):
		for iy, s in enumerate(row):
			result[iy][ix] = rules[to_tuple(s)]
	return np.concatenate([np.concatenate(row, axis=0) for row in result], axis=1)

state = to_array(".#./..#/###")
rules = {}

for line in fileinput.input():
	frm, to = map(to_array, line.strip().split(' => '))
	for _ in range(2):
		for _ in range(4):
			rules[to_tuple(frm)] = to
			frm = np.rot90(frm)
		frm = np.flipud(frm)

print_matrix(state)
for _ in range(18):
	state = find_next_state(state)
	print(np.count_nonzero(state))
