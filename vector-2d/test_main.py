import math
import unittest

from main import Vector2D


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.test_vector = Vector2D(2, 3)

    def test_repr(self):
        repr_str = repr(self.test_vector)
        assert repr_str == "Vector2D(x=2, y=3)"

    def test_str(self):
        repr_str = str(self.test_vector)
        assert repr_str == "Vector2D | X:2, Y:3"

    def test_add(self):
        vector_to_add = Vector2D(5, 7)
        added_vector = self.test_vector + vector_to_add

        assert added_vector.x == 7
        assert added_vector.y == 10

    def testMul(self):
        pass

    def testAbs(self):
        pass
