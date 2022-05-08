#! /usr/local/bin/python

import sys
import math
sys.path.insert(1, './utils')

from mathutils import distinct_primes

def is_10_primitive_root(denom):
	to_check = denom - 1
	result = distinct_primes(to_check)
	unique = list(set(result))
	powers = list(map(lambda x: int(to_check / x), unique))

	result = False

	for p in powers:
		if 10**p % denom == 1:
			is_10_primitive_root = True		

	return result


args = list(map(lambda item: int(item), sys.argv[1:]))
print(args)
denom = args[0]
print(unique)
print(powers)
print('10 is primitive root for %d? %s' % (denom, is_10_primitive_root))
