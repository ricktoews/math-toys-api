import unittest

import sys
sys.path.insert(1, '..')
from modules.calc_decimal import calc_decimal

class TestCalcDecimal(unittest.TestCase):

	def test_1_5_period(self):
		result = calc_decimal(1, 5, 10)
		self.assertEqual(result['period'], '2', "Should be '2'")

	def test_1_5_non_repeating(self):
		result = calc_decimal(1, 5, 10)
		self.assertEqual(result['non_repeating'], '2', "Should be '2'")

	def test_1_5_repeating(self):
		result = calc_decimal(1, 5, 10)
		self.assertEqual(result['repeating'], ' ', "Should be ' '")

	def test_1_5_period_length(self):
		result = calc_decimal(1, 5, 10)
		self.assertEqual(result['period_length'], '1', "Should be '1'")

if __name__ == '__main__':
	unittest.main()


