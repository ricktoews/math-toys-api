import sys
import math
sys.path.insert(1, '..')

from modules.utils.mathutils import is_relative_prime

# Imagine a c x c square. The outer layer is c + (c-1). The next is (c-1)+(c-2), and so on.
# This function inspects sums of layers, from the outer inward; and it gathers sums that
# are square.
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


def triples_for_c(c_list):
	triples = []
	for num in c_list:
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
					triple = { "a": a, "b": b, "c": c }
					if is_relative_prime(a, b):
						primes = primes + 1
						triples.append({ "triple": triple, "prime": True })
					else:			
						triples.append({ "triple": triple, "prime": False })
				used.append(a)
				used.append(b)
				n = n + 1

	return triples
