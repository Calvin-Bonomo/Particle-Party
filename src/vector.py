import math

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def addVector(self, v2):
        self.x += v2.x
        self.y += v2.y

    def subtractVector(self, v2):
        self.x -= v2.x
        self.y -= v2.y

    def scalarDivide(self, s):
        self.x /= s
        self.y /= s

    def scalarMultiply(self, s):
        self.x *= s
        self.y *= s
    
    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        mag = self.magnitude()
        self.scalarDivide(mag)
    
    def perp1(self):
        tempX = self.x
        self.x = self.y
        self.y = -tempX

    def perp2(self):
        tempX = self.x
        self.x = -self.y
        self.y = tempX