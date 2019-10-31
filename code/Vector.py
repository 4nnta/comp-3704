class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # return dot product of self with vector other
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # return cross product of self with vector other
    def cross(self, other):
        return self.x * other.y - other.x * self.y
