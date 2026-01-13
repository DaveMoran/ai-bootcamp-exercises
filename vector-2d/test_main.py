import math
import unittest

from main import Vector2D


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.testVector = Vector2D(2, 3)

    def test_repr(self):
        repr_str = repr(self.testVector)
        assert repr_str == "Vector2D(x=2, y=3)"

    def test_str(self):
        repr_str = str(self.testVector)
        assert repr_str == "Vector2D | X:2, Y:3"

    def testAdd(self):
        pass

    def testMul(self):
        pass

    def testAbs(self):
        pass
