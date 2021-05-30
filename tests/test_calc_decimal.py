import unittest

import sys
sys.path.insert(1, '..')
from modules.calc_decimal import calc_decimal

class TestCalcDecimal(unittest.TestCase):

	def test_1_5(self):
		result = calc_decimal(1, 5, 10)
		self.assertEqual(result['period'], '2', "Should be '2'")

	def test_1_7(self):
		result = calc_decimal(1, 7, 10)
		self.assertEqual(result['period'], '142857', "Should be '142857'")

	def test_1_11(self):
		result = calc_decimal(1, 11, 10)
		self.assertEqual(result['period'], '09', "Should be '09'")

	def test_1_12(self):
		result = calc_decimal(1, 12, 10)
		self.assertEqual(result['period'], '083', "Should be '083'")

if __name__ == '__main__':
	unittest.main()


