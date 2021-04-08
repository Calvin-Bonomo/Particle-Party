import vector
from vector import Vector
import numpy
import math

class Wall:
    def __init__(self, start, end, up):
        self.start = Vector(start[0], start[1])
        self.end = Vector(end[0], end[1])
        self.line = Vector(end[0] - start[0], end[1] - start[1])
        self.normal = Vector(start[0] - end[0], start[1] - end[1])
        self.normal.normalize()
        self.up = up
        if (up):
            self.normal.perp1()
        else:
            self.normal.perp2()