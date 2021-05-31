from modules.non_repeating import tally

# If all factors of the denominator are factors of the base, the expected result is -1.
# In this circumstance, the literal number of non-repeating digits is, of course, the
# length of the period. However, the non_repeating function returns -1 in such cases
# in order to distinguish from repeating periods that have a certain number of non-repeating
# digits.

# Base 10
def test_nr_5_10():
	result = tally(5, 10)
	assert result == -1

def test_nr_16_10():
	result = tally(16, 10)
	assert result == -1

def test_nr_50_10():
	result = tally(50, 10)
	assert result == -1

# If some factors of the denominator are not factors of the base, the expected result is
# the maximum count of the distinct factors that are also factors of the base.
# For example: for 60, the factors are 2*2*3*5. The factors in common with the base (10) are
# 2 and 5, and the maximum count of these is 2, since there are two instances of 2 and only one of 5.
def test_nr_60_10():
	result = tally(60, 10)
	assert result == 2

# If the denominator and the base are relative primes, the expected result is 0.
def test_nr_7_10():
	result = tally(7, 10)
	assert result == 0

def test_nr_39_10():
	result = tally(39, 10)
	assert result == 0
