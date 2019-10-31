import math
import collections

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "P(%s, %s)"%(self.X, self.Y)

    def __getitem__(self, item):
        ret = Point(self.X, self.Y)
        return ret

# calculating the cross product of 2 vectors
# same thing are stored for vector and point, so I'm reusing the Point class, if more vector is used, I will make a seperated class for it
def cross(v1: Point, v2: Point) -> int:
    return v1.X*v2.Y - v2.X*v1.Y

# calculating the turn of points p, q, r
def turn(p: Point, q: Point, r: Point) -> int:
    v1 = Point(q.X-p.X, q.Y-p.Y)
    v2 = Point(r.X-p.X, r.Y-p.Y)
    return cross(v1, v2)

# return 1 if CCW
# return -1 if CW
def isCW(verticesList) -> int:
    chosen = 0
    lowestY = math.inf
    highestX = -math.inf
    
    # finding point with lowest y (in case of tie, highest x)
    for i in range(len(verticesList)):
        if (verticesList[i].Y < lowestY):
            chosen = i
            lowestY = verticesList[i].Y
        elif (verticesList[i].Y == lowestY) and (verticesList[i].X > highestX):
            chosen = i
            highestX = verticesList[i].X

    # point previous to chosen and after chosen
    prev = chosen-1
    next = (chosen+1) % len(verticesList)

    rotation = turn(verticesList[prev], verticesList[chosen], verticesList[next])

    # print("{} {} {}".format(rotation, verticesList[chosen].X, verticesList[chosen].Y))

    if (rotation > 0):
        return 1
    else:
        return -1

if __name__ == '__main__':
    n = input("input the number of vertices: ")
    vertices = []
    print ("input the vertices in \"x y\" format:")
    for i in range(int(n)):
        x, y = input().split()
        p = Point(int(x), int(y))
        vertices.append(p)

    if (isCW(vertices) < 0):
        print("polygon is in CW order")
    else:
        print("polygon is in CCW order")
