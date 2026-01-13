class Vector2D:
    def __init__(self, numOne, numTwo):
        self.vector = (numOne, numTwo)

    def __repr__(self):
        return f"Vector2D(vector=({self.vector[0]},{self.vector[1]})"
