import unittest
import sys

sys.path.insert(1, '..')
from modules.non_repeating import tally

class TestNonRepeating(unittest.TestCase):

    def test_5_10(self):
        self.assertEqual(tally(5, 10), 0, "Should be 0")

    def test_6_10(self):
        self.assertEqual(tally(6, 10), 1, "Should be 1")

    def test_7_10(self):
        self.assertEqual(tally(7, 10), 0, "Should be 0")

    def test_8_10(self):
        self.assertEqual(tally(8, 10), 3, "Should be 3")

if __name__ == '__main__':
    unittest.main()

