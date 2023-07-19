#!/usr/bin/python3
"""Test module"""
from models.rectangle import Rectangle
from models.square import Square
import unittest


class test_base(unittest.TestCase):
    """test base module"""

    def test_1(self):
        r1 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r2.id, 12)
