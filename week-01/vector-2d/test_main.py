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

    def test_mul(self):
        mult_vector = self.test_vector * 4

        assert mult_vector.x == 8
        assert mult_vector.y == 12

    def test_abs(self):
        abs_vector = abs(self.test_vector)
        rounded_vec = round(abs_vector, 3)
        assert rounded_vec == 3.606
