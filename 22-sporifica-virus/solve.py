import numpy as np
import fileinput
from operator import add
from tqdm import tqdm

def vadd(*vs):
	return tuple(map(add, *vs))

def print_matrix(m):
	for row in m:
		print(''.join(row))

def main(part):
	extra = 100
	infections = 0
	grid = np.array([list(line.strip()) for line in fileinput.input()])
	pos = tuple(map(lambda x: x// 2, grid.shape))
	dir = (-1, 0)
	for _ in tqdm(range(10000000)):
		height, width = grid.shape
		# expand grid if needed
		if pos[0] == -1:
			pos = (extra, pos[1])
			new_row = np.full((extra+1, width), '.')
			grid = np.vstack((new_row, grid))

		elif pos[0] >= height:
			new_row = np.full((extra+1, width), '.')
			grid = np.vstack((grid, new_row))

		elif pos[1] == -1:
			pos = (pos[0], extra)
			new_col = np.full((height, extra+1), '.')
			grid = np.hstack((new_col, grid))

		elif pos[1] >= width:
			new_col = np.full((height, extra+1), '.')
			grid = np.hstack((grid, new_col))

		# do ant things
		if part == 1:
			if grid[pos] == '#':
				dir = (dir[1], -dir[0])
				grid[pos] = '.'
			elif grid[pos] == '.': 
				dir = (-dir[1], dir[0])
				grid[pos] = '#'
				infections += 1

		if part == 2:
			if grid[pos] == '.':
				dir = (-dir[1], dir[0])
				grid[pos] = 'W'
			elif grid[pos] == 'W': 
				grid[pos] = '#'
				infections += 1
			elif grid[pos] == '#':
				dir = (dir[1], -dir[0])
				grid[pos] = 'F'
			elif grid[pos] == 'F':
				dir = (-dir[0], -dir[1])
				grid[pos] = '.'


		pos = vadd(pos, dir)
	return infections
print(main(2))



