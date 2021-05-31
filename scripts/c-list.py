#! /usr/local/bin/python

import sys
import math
sys.path.insert(1, './utils')

from mathutils import PRIMES, is_relative_prime

def find_layers(c):
	result = []
	layer_sum = 0
	layer = c * 2 - 1
	while layer > 5:
		layer_sum = layer_sum + layer
		sq_root = math.sqrt(layer_sum)
		if sq_root.is_integer():
			result.append(layer_sum)
		layer = layer - 2

	return result


numlist = PRIMES[2:10]
numlist = range(5, 100)

for num in numlist:
	a_squares = find_layers(num)
	if len(a_squares) > 0:
		used = []
		n = 1
		primes = 0
		for a_square in a_squares:
			a = int(math.sqrt(a_square))
			c = num
			b = int(math.sqrt(num**2 - a_square))
			if not a in used and not b in used:
				if is_relative_prime(a, b):
					primes = primes + 1
					print(f'{n}. triple ({a}, {b}, {c}) => {a*a} + {b*b} = {c*c}, (prime {primes})')
				else:			
					print(f'{n}. triple ({a}, {b}, {c}) => {a*a} + {b*b} = {c*c}')
			used.append(a)
			used.append(b)
			n = n + 1
		print('-------------------------------')


