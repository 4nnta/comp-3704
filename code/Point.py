import Vector

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # return a vector with self as head, other point as tail
    def getVector(self, other):
        return Vector(self.x - other.x, self.y - other.y)
