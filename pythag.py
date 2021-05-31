from modules.get_triples import get_triples
from utils.mathutils import PRIMES

data = get_triples(PRIMES[2:20])
print(data)
