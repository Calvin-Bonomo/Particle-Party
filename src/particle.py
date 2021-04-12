import numpy as np
import vector
from vector import Vector
import pygame
import wall
from wall import Wall
import math
import copy

class Particle:
    def __init__(self, size, position, velocity, mass):
        self.size = size
        self.velocity = Vector(velocity[0], velocity[1])
        self.position = Vector(position[0], position[1])
        self.mass = mass

    def move(self, acceleration):
        acceleration.scalarDivide(self.mass)
        self.velocity.addVector(acceleration)
        self.position.addVector(self.velocity)
    
    def update(self, walls, acceleration, friction):
        # Move by a given acceleration
        self.move(Vector(acceleration[0], acceleration[1]))

        # Iterate through all walls
        # and check for collisions
        for wall in walls:
            # Don't check walls if
            # they're too far from
            # a particle
            wallToLine = vector.subtract(wall.start, self.position)
            if (vector.magnitude(wallToLine) > vector.magnitude(wall.line)):
                continue

            # If the returned value is
            # greater than 0, the ball
            # is colliding with the wall
            clipVal = self.intersectsWall(wall)

            if (clipVal > 0):
                # Move the particle out of the wall
                dPos = vector.multiply(wall.normal, clipVal)
                self.position.addVector(dPos)

                # Bounce the particle off of the wall
                self.velocity = self.getReflection(copy.copy(wall.normal))

                # Reduce the particle's velocity by
                # the friction coefficient
                self.velocity.scalarMultiply(friction)
            
    def getReflection(self, normal):
        # Get the dot product of the
        # wall's normal and the
        # particle's velocity
        wallNormalDot = vector.dot(self.velocity, normal)
        
        # Multiply the dot
        # product by 2
        wallNormalDot *= 2

        # Scale the normal by the
        # doubled dot product
        normal.scalarMultiply(wallNormalDot)

        # Subtract the scaled normal
        # from the velocity to get
        # the reflection vector
        reflection = vector.subtract(self.velocity, normal)

        # Return the reflection
        return reflection
    
    def intersectsWall(self, wall1):
        # Get the directional vector
        # representing the wall
        wallDir = vector.normalize(wall1.line)

        # Get the length of the line
        # from the start of the wall
        # to the nearest point to the ball
        projectedMag = vector.dot(wallDir, vector.subtract(self.position, wall1.start))

        # Scale the directional vector
        # by the projected magnitude
        wallDir.scalarMultiply(projectedMag)

        # Get the line between the
        # ball and the nearest point on the wall
        wallToBall = vector.subtract(vector.add(wallDir, wall1.start), self.position)

        # Return the amount the wall
        # is intersecting with the ball
        return self.size - vector.magnitude(wallToBall)