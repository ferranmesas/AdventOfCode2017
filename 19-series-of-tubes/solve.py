import fileinput
import re
from operator import add
from string import ascii_letters

maze = [list(l.rstrip('\n')) for l in fileinput.input()]

pos = (0, maze[0].index('|'))
dir = (1, 0)
steps = 0
string = []
while maze[pos[0]][pos[1]] != ' ':
	steps += 1
	pos = tuple(map(add, pos, dir))
	if maze[pos[0]][pos[1]] in ascii_letters:
		string.append(maze[pos[0]][pos[1]])
	if maze[pos[0]][pos[1]] == '+':
		if maze[pos[0] + dir[1]][pos[1] + dir[0]] != ' ':
			dir = (dir[1], dir[0])
		elif maze[pos[0] - dir[1]][pos[1] - dir[0]] != ' ':
			dir = (-dir[1], -dir[0])

print(''.join(string), steps)
