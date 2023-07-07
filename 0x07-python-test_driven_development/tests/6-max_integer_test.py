#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])
      """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer1(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer2(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer4(self):
        self.assertEqual(max_integer([-10, -10, -10, -10]), -10)

    def test_max_integer5(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_max_integer3(self):
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

    def test_max_integer6(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_max_integer13(self):
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), None)
