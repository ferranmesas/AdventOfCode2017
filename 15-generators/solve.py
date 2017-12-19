from itertools import islice

def g(initial, factor, test):
	m = 2147483647
	n = initial
	while True:
		n = (n * factor) % m
		if n % test == 0:
			yield n

total = 0
for a, b in islice(zip(g(116,16807, 4), g(299, 48271, 8)), 5000000):
	total += a & 0xffff == b & 0xffff

print(total)
