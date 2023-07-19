#!/usr/bin/python3
"""Test module"""
from models.rectangle import Rectangle
import unittest


class test_base_rectangle1(unittest.TestCase):
    """test base module"""

    """ area """
    def test_1(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_2(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

    def test_3(self):
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_4(self):
        r4 = Rectangle(8, 7, 0)
        self.assertEqual(r4.area(), 56)

    def test_5(self):
        r5 = Rectangle(8, 7, 0, 0)
        self.assertEqual(r5.area(), 56)

    def test_6(self):
        with self.assertRaises(ValueError):
            r6 = Rectangle(-3, 2)
            r6.area()

    def test_7(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(1.3, 2)
            r7.area()
    def test_8(self):
        with self.assertRaises(TypeError):
            r8 = Rectangle([])

    def test_9(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle({})

    def test_10(self):
        with self.assertRaises(TypeError):
            r10 = Rectangle("string")

    def test_11(self):
        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2)
            r11.area()

    def test_12(self):
        with self.assertRaises(ValueError):
            r12 = Rectangle(3, 0)
            r12.area()

    def test_13(self):
        with self.assertRaises(ValueError):
            r13 = Rectangle(8, 7, -1, 0)
            r13.area()

    def test_14(self):
        with self.assertRaises(ValueError):
            r14 = Rectangle(8, 7, 0, -1)
            r14.area()

    def test_15(self):
        with self.assertRaises(TypeError):
            r15 = Rectangle(8, 7, 0, 'infi')
            r15.area()

    def test_16(self):
        with self.assertRaises(TypeError):
            r16 = Rectangle()
            r16.area()

    def test_18(self):
        with self.assertRaises(TypeError):
            r18 = Rectangle(8, 7, 0, 'nan')
            r18.area()

    def test_19(self):
        with self.assertRaises(TypeError):
            r19 = Rectangle(8, 7, 0, {})
            r19.area()
