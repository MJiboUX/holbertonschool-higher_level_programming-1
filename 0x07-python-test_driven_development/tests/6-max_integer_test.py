#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_last(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Should be 4")

    def test_max_first(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4, "Should be 4")

    def test_max_mid(self):
        self.assertEqual(max_integer([1, 4, 2]), 4, "Should be 4")

    def test_max_one_negative(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4, "Should be 4")

    def test_max_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1, "Should be -1")

    def test_max_one_elem(self):
        self.assertEqual(max_integer([4]), 4, "Should be 4")

    def test_max_empty_list(self):
        self.assertEqual(max_integer([]), None, "Should be None")

if __name__ == '__main__':
    unittest.main()
