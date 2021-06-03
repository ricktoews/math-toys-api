import math
from modules.utils.build_pascal import build_triangle

PASCAL = build_triangle()

def get_phi_power(power):
	whole = 0
	root = 0
	cancel = 2**(power - 1)
	jacked_terms = []
	for i in range(0, power+1):
		if i%2 == 0:
			add = PASCAL[power][power-i] * 5**(i/2)
			whole += add
		else:
			add = PASCAL[power][power-i] * 5**((i - 1)/2)
			root += add
	# at this point, we have two sums: the whole part, and the coefficient
	# for the square root of 5. Since the denominator is going to be 2,
	# we must cancel out the appropriate power of 2 from the numerator.
	whole /= cancel
	root /= cancel
	real_value = ((math.sqrt(5) + 1) / 2) ** power
	fib_approx = real_value / math.sqrt(5)
	payload = {
		'power': power,
		'phi_num': { 'whole': int(whole), 'sqrt_5_coef': int(root) },
		'real_value': real_value,
		'fib_approx': fib_approx
	}
	return payload