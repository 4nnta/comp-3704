import math

"""""""""""""""
Helper class
"""""""""""""""
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Vector:
    # init a vector p2 - p1
    def __init__(self, p1: Point, p2: Point):
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y

class Polygon:
    def __init__(self, pointList: list):
        self.pList = pointList

    def __getitem__(self, item: int):
        return self.pList[item]

    def size(self):
        return len(self.pList)

# return cross product of 2 vector
def cross(v1: Vector, v2: Vector) -> float:
    return v1.x * v2.y - v2.x * v1.y

# return turn of p, q, r
# return 1 for left turn
# return -1 for right turn
# return 0 for colinear
def turn(p: Point, q: Point, r: Point) -> int:
    v1 = Vector(p, q)
    v2 = Vector(p, r)
    crossProduct = cross(v1, v2)

    if (crossProduct > 0):
        return 1
    elif (crossProduct < 0):
        return -1
    else:
        return 0
"""""""""""""""
End of helper class
"""""""""""""""

"""""""""""""""
Spawning a random convex polygon using convex hull (Jarvis's algorithm O(nh)), for driver test
code taken from GeeksForGeek
"""""""""""""""
def Left_index(points): 
    minn = 0
    for i in range(1,len(points)): 
        if points[i].x < points[minn].x: 
            minn = i 
        elif points[i].x == points[minn].x: 
            if points[i].y > points[minn].y: 
                minn = i 
    return minn 
  
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y) 
  
    if val == 0: 
        return 0
    elif val > 0: 
        return 1
    else: 
        return 2
  
def convexHull(points, n): 
      
    # There must be at least 3 points  
    if n < 3: 
        return
  
    # Find the leftmost point 
    l = Left_index(points) 
  
    hull = [] 
    
    p = l 
    q = 0
    while(True): 
          
        # Add current point to result  
        hull.append(points[p]) 
  
        q = (p + 1) % n 
  
        for i in range(n): 
              
            # If i is more counterclockwise  
            # than current q, then update q  
            if(orientation(points[p],  
                           points[i], points[q]) == 2): 
                q = i 
  
        p = q 
  
        # While we don't come to first point 
        if(p == l): 
            break
  
    # Print Result  
    return hull

# input number of maximum vertices as the parameter
def getPolygon(n: int):
    import random
    pointList = []

    for i in range(n):
        x = random.randint(1, 200)
        y = random.randint(1, 200)
        pointList.append(Point(x, y))

    hull = convexHull(pointList, n)
    return Polygon(hull)

def getOutsidePoint(poly: Polygon):
    import random

    # return a random point outside of the polygon
    # by taking the extreme right-most vertex of the polygon, extend the x-coordinate, and random the y-coordinate

    extremeRight = 0

    for i in range(poly.size()):
        if (poly[i].x > poly[extremeRight].x):
            extremeRight = i

    x = poly[extremeRight].x + 100
    y = random.randint(-100, 100)
    return Point(x, y)
"""""""""""""""
End of spawning polygon
"""""""""""""""

"""""""""""""""
Function of finding left tangent
"""""""""""""""
# check the state of vertex origin^th considering point P
# return "vis" if vertex origin^th is visible to P
# "    " "inv" "                    " invisible to P
# return "left" if vertex origin^th is left tangent to P
# return "right" if vertex origin^th is right tangent to P
def checkState(poly: Polygon, origin: int, P: Point) -> str:
    prev = origin-1
    next = (origin+1) % poly.size()

    turnPrev = turn(P, poly[origin], poly[prev])
    turnNext = turn(P, poly[origin], poly[next])

    # if both turn is right, then we get the left tangent
    if (turnPrev <= 0) and (turnNext == -1):
        return "left"

    # if both turn is left, then we get the right tangent
    if (turnPrev >= 0) and (turnNext == 1):
        return "right"

    # if prev turn is right, and next turn is left, we get a visible state
    if (turnPrev == -1) and (turnNext == 1):
        return "vis"

    # if prev turn is left, and next turn is right, we get an invis state
    if (turnPrev == 1) and (turnNext == -1):
        return "inv"

# function comes with an O(n) solution to check for correcness of O(log n) solution
def getLeftTangent(poly: Polygon, P: Point) -> int:
    # n = size of polygon
    n = poly.size()

    # O(n) solution for checking correctness
    for i in range(n):
        if (checkState(poly, i, P) == 'left'):
            print("O(n) solution returns {} as the left tangent".format(poly[i]))

    # O(log n) solution
    low, high = 0, n-1
    ret = 0

    while (low <= high):
        mid = math.floor((high + low) / 2)

        if (checkState(poly, low, P) == 'left'):
            ret = low
            break
        elif (checkState(poly, high, P) == 'left'):
            ret = high
            break
        elif (checkState(poly, mid, P) == 'left'):
            ret = mid
            break

        if (checkState(poly, mid, P) == checkState(poly, low, P)):
            low = mid+1
        else:
            high = mid-1

    print("O(log n) solution returns {} as the left tangent".format(poly[ret]))

    return ret
"""""""""""""""
End of finding left tangent
"""""""""""""""

"""""""""""""""
Driver
"""""""""""""""
if __name__ == "__main__":
    """ Custom polygon, un-comment this to input other test case
    n = input("input the number of vertices: ")
    vertices = []

    print ("input the vertices in \"x y\" format:")
    for i in range(int(n)):
        x, y = input().split()
        p = Point(float(x), float(y))
        vertices.append(p)

    poly = Polygon(vertices)
    x, y = input("input point outside of polygon: ").split()
    P = Point(float(x), float(y))

    test = getLeftTangent(poly, P)
    """

    print("testing finding left tangent, driver will generate a random polygon with input maximum number of vertices, and a point outside of the polygon.")
    print("there are 2 algorithms running, O(n) is for checking the correctness of algorithm, and O(log n) is the actual homework.")
    n = input("input the max number of vertices: ")
    poly = getPolygon(int(n))
    outPoint = getOutsidePoint(poly)
    test = getLeftTangent(poly, outPoint)


        







    
