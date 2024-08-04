from collatz.algorithms import *
import unittest

class TestCollatzAlgorithms(unittest.TestCase):
    def test_check_collatz(self):
        self.assertTrue(check_collatz(1))
        self.assertTrue(check_collatz(2))
        self.assertTrue(check_collatz(3))
        self.assertTrue(check_collatz(67))

if __name__ == "__main__":
    unittest.main()