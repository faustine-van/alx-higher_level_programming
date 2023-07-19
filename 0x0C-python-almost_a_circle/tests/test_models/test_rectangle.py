#!/usr/bin/python3
"""Test module"""
from models.rectangle import Rectangle
import unittest


class test_base_rectangle(unittest.TestCase):
    """test base module"""

    @classmethod
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    """ id """
    def test_1(self):
        r2 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_2(self):
        r3 = Rectangle(2, 10, 0, 0, -12)
        self.assertEqual(r3.id, -12)

    def test_3(self):
        r3 = Rectangle(2, 10, 0, 0, [])
        self.assertEqual(r3.id, [])

    def test_4(self):
        r4 = Rectangle(2, 10, 0, 0, [0])
        self.assertEqual(r4.id, [0])

    def test_5(self):
        r3 = Rectangle(2, 10, 0, 0, {})
        self.assertEqual(r3.id, {})

    def test_6(self):
        r6 = Rectangle(2, 10, 0, 0, {"id": 1})
        self.assertEqual(r6.id, {"id": 1})

    def test_7(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(2)
    """width and height"""

    def test_8(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "2")

    def test_width(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle("10", 2)

    def test_width_is_0(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 2)

    def test_height_is_0(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 0)

    def test_height_is_0_less(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 0)
            r4.height = -10

    def test_width_less_0(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "2")
            r4.width = -10

    def test_height_float(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 1.2)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(1.0, 2)

    def test_width_list(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle([], 2)

    def test_width_list_witt_item(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle([0], 2)

    def test_width_dict(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle({}, 2)

    def test_width_dict(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, '1')
    """x and y"""
    def test_10(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

    def test_11(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = []

    def test_12(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = 1.2

    def test_13(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = "string"

    def test_14(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = 'a'

    def test_15(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.y = {}

    def test_16(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.y = []

    def test_17(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.y = 1.2

    def test_18(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.y = "string"

    def test_14(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = 'a'

    def test_(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)

    def test_(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -3, 1)

    def test__(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, -2, 3, 1)

    def test_19(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 3, [])
