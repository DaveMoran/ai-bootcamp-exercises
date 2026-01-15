"""
Exercise 2: 2D Vector Class

An X/Y Vector class that can be used for displaying points on a graph
"""

import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __str__(self):
        return f"Vector2D | X:{self.x}, Y:{self.y}"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)
