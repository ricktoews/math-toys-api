import math
from modules.utils.mathutils import is_relative_prime

MAX_TRIPLES_IN_SET = 10

def make_triple(a, b):
    c_squared = a**2 + b**2
    triple = { 'a': a, 'b': b, 'c': int(math.sqrt(c_squared)) }
    return triple

# corner = (c - b)^2.
# Let n = sqrt(corner).
# Then a^2 = n*n + 2*b*n, or n(n + 2b).
# 
# Let corner = 1.
# Then n = sqrt(corner) = 1.
# Then a^2 = 1 + 2b.
# So b is any of the set of values for which 1 + 2b is an integer square.
#
# Let corner = 4.
# Then n = sqrt(corner) = 2.
# Then a^2 = 4 + 4b, or 4(1 + b).
# So b is any of the set of values for which 4(1 + b) is an integer square.
# And since 4 is itself square, b is any of the set of values for which (1 + b) is an integer square.
#
# 
def triples_for_c_minus_b(c_minus_b):
    b = 1
    triples = []
    while (len(triples) < MAX_TRIPLES_IN_SET):
        a_squared = c_minus_b * (c_minus_b + 2 * b)
        a = math.sqrt(a_squared)
        if a.is_integer() and a < b:
            triple = make_triple(int(a), b)
            prime = is_relative_prime(a, b)
            triples.append({ 'triple': triple, 'prime': prime })
        b += 1
    return triples
