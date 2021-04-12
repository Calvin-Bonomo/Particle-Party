import vector
from vector import Vector
import numpy
import math

class Wall:
    def __init__(self, start, end, up):
        self.start = Vector(start[0], start[1])
        self.end = Vector(end[0], end[1])
        self.line = Vector(end[0] - start[0], end[1] - start[1])
        self.normal = vector.normalize(self.line)
        self.up = up
        if (up):
            self.normal = vector.perp1(self.normal)
        else:
            self.normal = vector.perp2(self.normal)