#!/usr/bin/python3
"""Unittest script for max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function"""

    def test_empty_list(self):
        """Test case for an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_normal_list(self):
        """Test case for a normal list of ints"""
        normal = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(normal), 5)

    def test_max_first(self):
        """Test case for max int at the beginning of the list"""
        first = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(first), 5)

    def test_max_middle(self):
        """Test case for max int in middle of the list"""
        middle = [0, 4, 2, 1, 3]
        self.assertEqual(max_integer(middle), 4)

    def test_negatives_list(self):
        """Test case for negatives inclusive"""
        negs = [3, -7, 0, -1, -2]
        self.assertEqual(max_integer(negs), 3)

    def test_int_all_negs(self):
        """Test case for list of negative integers"""
        all_neg_int = [-2, -9, -12, -5]
        self.assertEqual(max_integer(all_neg_int), -2)

    def test_int_same(self):
        """Test case for list containing same integer"""
        same_face = [5, 5, 5, 5]
        self.assertEqual(max_integer(same_face), 5)

    def test_float_list(self):
        """Test case for list containing floats"""
        floats = [0.2, 0.6, 0.0, 20.5, 2.05]
        self.assertEqual(max_integer(floats), 20.5)

    def test_float_negs(self):
        """Test case for list containing negative floats"""
        neg_floats = [0.2, -0.6, 0.0, -20.5, 2.05]
        self.assertEqual(max_integer(neg_floats), 2.05)

    def test_float_all_negs(self):
        """Test case for list of negative floats"""
        all_neg_floats = [-2.5, -14.2, -1.0, -11.3]
        self.assertEqual(max_integer(all_neg_floats), -1.0)

    def test_only_the_one(self):
        """Test case for list containing only one element"""
        the_one = [5]
        self.assertEqual(max_integer(the_one), 5)

    def test_list_str(self):
        """Test case for list having int and string elements"""
        str_elements = [1, 6, "alx", 12, "25"]
        self.assertRaises(TypeError, max_integer, str_element)

    def test_list_all_str(self):
        """Test case for list of strings"""
        all_str = ["45", "abc", "stringy", "alx"]
        self.assertEqual(max_integer(all_str), "stringy")

    def test_nada(self):
        """Test case argument passed is not a list"""
        self.assertRaises(TypeError, max_integer, 5)


if __name__ == '__main__':
    unittest.main()
