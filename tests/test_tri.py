import unittest
import sys
sys.path.insert(1, '..')
from modules.tri import nth_triangular

class TestTri(unittest.TestCase):

    def test_tri1(self):
        self.assertEqual(nth_triangular(5), 15, "Should be 15")

    def test_tri2(self):
        self.assertEqual(nth_triangular(4), 6, "Should be 10")

if __name__ == '__main__':
    unittest.main()

