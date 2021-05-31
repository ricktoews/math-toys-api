import pytest
from modules.calc_decimal import calc_decimal

@pytest.fixture
def first():
	print("Set up first fixture")
	yield "not really needed, but an example of setting up a fixture. (appears if there's a test failure.)"
	print("Clean up first fixture")

# Tests for Base 10
# Non-repeating periods.
def test_1_5(first):
	result = calc_decimal(1, 5, 10)
	assert result['period'] == '2' and result['repeating'] == 0

def test_1_4():
	result = calc_decimal(1, 4, 10)
	assert result['period'] == '25' and result['repeating'] == 0

# Repeating periods, with non-repeating components.
def test_1_6():
	result = calc_decimal(1, 6, 10)
	assert result['period'] == '16' and result['non_repeating'] == '1'

def test_1_12():
	result = calc_decimal(1, 12, 10)
	assert result['period'] == '083' and result['non_repeating'] == '08'

def test_1_75():
	result = calc_decimal(1, 75, 10)
	assert result['period'] == '013' and result['non_repeating'] == '01'

# Repeating periods, with no non-repeating digits.
def test_1_7():
	result = calc_decimal(1, 7, 10)
	assert result['period'] == '142857' and result['repeating'] == 6

def test_1_13():
	result = calc_decimal(1, 13, 10)
	assert result['period'] == '076923' and result['repeating'] == 6

# Base 8
# Non-repeating period
def test_1_4_8():
	result = calc_decimal(1, 4, 8)
	assert result['period'] == '2' and result['repeating'] == 0

# Repeating period
def test_1_5_8():
	result = calc_decimal(1, 5, 8)
	assert result['period'] == '1463' and result['repeating'] == 4

# Base 16
# Non-repeating period
def test_1_2_16():
	result = calc_decimal(1, 2, 16)
	assert result['period'] == '8' and result['repeating'] == 0

# Repeating period
def test_1_17_16():
	result = calc_decimal(1, 17, 16)
	assert result['period'] == '0F' and result['repeating'] == 2
