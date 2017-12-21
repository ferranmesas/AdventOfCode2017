import re
import fileinput
from itertools import repeat
numbers = re.compile(r'[-0-9]+')

def parse(line):
	n = list(map(int, numbers.findall(line)))
	return (tuple(n[0:3]), tuple(n[3:6]), tuple(n[6:9]))

def manhattan(position):
	return sum(map(abs, position))

def eval_at(particle, t):
	return tuple(map(lambda p, v, a: p + (v * t) + (a * t * t), *particle))

particles = [parse(line) for line in fileinput.input()]

particles_at_time = list(map(eval_at, particles, repeat(300)))
closest = min(*particles_at_time, key=manhattan)

print(particles_at_time.index(closest))
