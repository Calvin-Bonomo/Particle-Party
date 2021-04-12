import math

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def add(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y)

def subtract(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y)

def divide(v, s):
    return Vector(v.x / s, v.y / s)

def multiply(v, s):
    return Vector(v.x * s, v.y * s)

def magnitude(v):
    return math.sqrt(v.x * v.x + v.y * v.y)

def normalize(v):
    mag = magnitude(v)
    return divide(v, mag)

def perp1(v):
    return Vector(v.y, -v.x)

def perp2(v):
    return Vector(-v.y, v.x)

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