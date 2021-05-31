import pytest
from modules.triples_c import triples_for_c
from modules.triples_c_minus_b import triples_for_c_minus_b

@pytest.fixture
def init_triples():
	triples = triples_for_c(range(5,500))
	yield triples

def test_c_prime(init_triples):
	triples = init_triples
	prime_triples = filter(lambda x: x['prime'] == True, triples)
	print('triples', prime_triples)
	triple = triples[0]['triple']
	assert triple['a'] == 3 and triple['b'] == 4 and triple['c'] == 5
