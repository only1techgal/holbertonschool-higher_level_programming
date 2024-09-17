#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_max_integer(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_mixed(self):
        """Test with a list of positive and negative integers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_max_integer_single(self):
        """Test with a single-element list"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_empty(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.3, 3.7]), 3.7)

    def test_max_integer_mixed_numbers(self):
        """Test with a list of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

if __name__ == '__main__':
    unittest.main()
