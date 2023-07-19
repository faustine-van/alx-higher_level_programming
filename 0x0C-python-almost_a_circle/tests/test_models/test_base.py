#!/usr/bin/python3
"""Test module"""
from models.base import Base
import unittest


class test_base(unittest.TestCase):
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

    def test_equal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_1(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_2(self):
        b = Base(40)
        self.assertEqual(b.id, 40)

    def test_3(self):
        b3 = Base(12)
        self.assertNotEqual(b3.id, 13)

    def test_4(self):
        b4 = Base(-1)
        self.assertEqual(b4.id, -1)

    def test_5(self):
        b5 = Base(100)
        self.assertEqual(b5.id, 100)

    def test_6_raise(self):
        with self.assertRaises(TypeError):
            Base("hello", 12)

    def test_6_1_raise(self):
        with self.assertRaises(TypeError):
            Base("hello", 12, 14)

    def test_7(self):
        c = Base([1, 12])
        self.assertEqual(c.id, [1, 12])

    def test_7_1(self):
        c = Base([])
        self.assertEqual(c.id, [])

    def test_8(self):
        c = Base((1, 12))
        self.assertEqual(c.id, (1, 12))

    def test_9(self):
        c = Base({"id": 1, "age": 12})
        self.assertEqual(c.id, {'id': 1, 'age': 12})
