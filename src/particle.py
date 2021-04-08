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
            wallToLine = Vector(wall.start.x - self.position.x, wall.start.y - self.position.y)
            if (wallToLine.magnitude() > wall.line.magnitude()):
                continue

            # If the returned value is
            # greater than 0, the ball
            # is colliding with the wall
            clipVal = self.intersectsWall(wall)

            if (clipVal > 0):
                # Move the particle out of the wall
                dPos = Vector(wall.normal.x, wall.normal.y)
                dPos.scalarMultiply(clipVal)
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
        wallNormalDot = self.velocity.x * normal.x + self.velocity.y * normal.y
        
        # Multiply the dot
        # product by 2
        wallNormalDot *= 2

        # Scale the normal by the
        # doubled dot product
        normal.scalarMultiply(wallNormalDot)

        # Subtract the scaled normal
        # from the velocity to get
        # the reflection vector
        reflection = copy.copy(self.velocity)
        reflection.subtractVector(normal)

        # Return the reflection
        return reflection
    
    def intersectsWall(self, wall1):
        # Get the directional vector
        # representing the wall
        wallDir = copy.copy(wall1.line)
        wallDir.normalize()

        # Get the length of the line
        # from the start of the wall
        # to the nearest point to the ball
        projectedMag = wallDir.x * (self.position.x - wall1.start.x) + wallDir.y * (self.position.y - wall1.start.y)

        # Scale the directional vector
        # by the projected magnitude
        wallDir.scalarMultiply(projectedMag)

        # Get the line between the
        # ball and the nearest point on the wall
        wallToBall = Vector((wallDir.x + wall1.start.x) - self.position.x, (wallDir.y + wall1.start.y) - self.position.y)

        # Return the amount the wall
        # is intersecting with the ball
        return self.size - wallToBall.magnitude()