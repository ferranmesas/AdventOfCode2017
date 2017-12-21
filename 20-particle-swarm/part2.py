import re
import fileinput
from itertools import repeat
from collections import Counter
from operator import add
numbers = re.compile(r'[-0-9]+')

class Particle:
	def __init__(self, p, v, a):
		self.p = p
		self.v = v
		self.a = a

	def step(self):
		self.v = tuple(map(add, self.v, self.a))
		self.p = tuple(map(add, self.p, self.v))
		return self.p
	def __repr__(self):
		return "p={self.p} v={self.v} a={self.a}".format(self=self)

def parse(line):
	n = list(map(int, numbers.findall(line)))
	return Particle(tuple(n[0:3]), tuple(n[3:6]), tuple(n[6:9]))

def manhattan(position):
	return sum(map(abs, position))

particles = [parse(line) for line in fileinput.input()]

for i in range(1000):
	positions = Counter(map(lambda p: p.step(), particles))
	for k, v in positions.items():
		if v > 1:
			print("Collision")
			particles = [p for p in particles if p.p != k]
print(len(particles))