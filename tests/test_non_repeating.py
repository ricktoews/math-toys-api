import unittest
import sys

sys.path.insert(1, '../modules')
from non_repeating import tally

class TestTri(unittest.TestCase):

    def test_5_10(self):
        self.assertEqual(tally(5, 10), 0, "Should be 0")

    def test_6_10(self):
        self.assertEqual(tally(6, 10), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()

