import numpy
import vector
from vector import Vector
from random import seed
from random import random
import time
import math

class Emitter:
    def __init__(self, maxParticles, lifeTime, maxSize, minSize, randomness, pType, position):
        self.maxParticles = maxParticles
        self.lifeTime = lifeTime
        self.maxSize = maxSize
        self.minSize = minSize
        self.randomness = randomness
        self.particles = []
        self.pLifeTimes = []
        self.startTimes = []
        self.position = position
        self.pType = pType
        self.theta = 0
        self.velocity = 0
        self.dir = Vector(1, 0)
        seed(time.ctime)
        for _ in range(maxParticles):
            self.createParticle()

    def getRandomVal(self, randomness):
        randVal = random()
        while (randVal < 0.1):
            randVal = random()
        if (randVal < self.randomness):
            randVal = randVal + (1 - self.randomness)
        
        return randVal

    def update(self, maxParticles, minSize, theta, velocity):
        self.minSize = minSize
        deltaP = maxParticles - self.maxParticles
        totalP = abs(deltaP)

        theta *= math.pi/180.0
        self.velocity = velocity
        if (self.theta != theta):
            self.theta = theta
            self.dir.x = math.cos(theta) - math.sin(theta)
            self.dir.y = (math.sin(theta) + math.cos(theta)) - 1

        while (self.maxParticles != maxParticles):
            if (self.maxParticles > maxParticles):
                self.destroyParticle()
            else:
                self.createParticle()
            
            self.maxParticles += deltaP/totalP
        
        for i in range(maxParticles):
            currentTime = time.time()

            if (self.startTimes[i] + self.pLifeTimes[i] <= currentTime):
                self.replaceParticle(i)

    def createParticle(self):
        currentTime = time.time()
        self.startTimes.append(currentTime)
        self.pLifeTimes.append(self.lifeTime * self.getRandomVal(self.randomness))
        self.particles.append(self.pType(self.minSize + (self.maxSize - self.minSize) * self.getRandomVal(self.randomness), self.position, [self.dir.x * (self.velocity * self.getRandomVal(self.randomness)), self.dir.y * (self.velocity * self.getRandomVal(self.randomness))], self.getRandomVal(self.randomness)))

    def replaceParticle(self, i):
        currentTime = time.time()
        self.startTimes[i] = currentTime
        self.pLifeTimes[i] = self.lifeTime * self.getRandomVal(self.randomness)
        self.particles[i] = self.pType(self.minSize + (self.maxSize - self.minSize) * self.getRandomVal(self.randomness), self.position, [self.dir.x * (self.velocity * self.getRandomVal(self.randomness)), self.dir.y * (self.velocity * self.getRandomVal(self.randomness))], self.getRandomVal(self.randomness))

    def destroyParticle(self):
        self.startTimes.pop()
        self.pLifeTimes.pop()
        self.particles.pop()