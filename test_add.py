# test_add.py
import unittest
from add import add

class TestAddFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10, -5), 5)

if __name__ == '__main__':
    unittest.main()
