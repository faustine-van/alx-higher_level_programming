#!/usr/bin/python3
"""Test module"""
from models.square import Square
import unittest


class test_base_Square(unittest.TestCase):
    """test base module"""

    """ area """
    def test_1(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_2(self):
        r2 = Square(5)
        self.assertEqual(r2.area(), 25)

    def test_3(self):
        r3 = Square(2, 2)
        self.assertEqual(r3.area(), 4)

    def test_4(self):
        r4 = Square(3, 1, 3)
        self.assertEqual(r4.area(), 9)

    def test_5(self):
        r5 = Square(8, 8, 0, 0)
        self.assertEqual(r5.area(), 64)

    def test_6(self):
        with self.assertRaises(ValueError):
            r6 = Square(-3, 2)
            r6.area()

    def test_7(self):
        with self.assertRaises(TypeError):
            r7 = Square(1.3, 2)
            r7.area()

    def test_8(self):
        with self.assertRaises(TypeError):
            r8 = Square([])

    def test_9(self):
        with self.assertRaises(TypeError):
            r9 = Square({})

    def test_10(self):
        with self.assertRaises(TypeError):
            r10 = Square("string")

    def test_11(self):
        with self.assertRaises(ValueError):
            r11 = Square(0, 2)
            r11.area()

    def test_12(self):
        with self.assertRaises(ValueError):
            r12 = Square(-3)
            r12.area()

    def test_13(self):
        with self.assertRaises(ValueError):
            r13 = Square(8, 7, -1, 0)
            r13.area()

    def test_14(self):
        r14 = Square(8, 7, 0, -1)
        self.assertEqual(r14.area(), 64)

    def test_15(self):
        with self.assertRaises(TypeError):
            r15 = Square('infi')
            r15.area()

    def test_16(self):
        with self.assertRaises(TypeError):
            r16 = Square()
            r16.area()

    def test_18(self):
        with self.assertRaises(TypeError):
            r18 = Square('nan')
            r18.area()

    def test_19(self):
        with self.assertRaises(TypeError):
            r19 = Square({})
            r19.area()
