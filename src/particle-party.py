import numpy as np
import pygame
import emitter
from emitter import Emitter
import particle
from particle import Particle
import time
import wall
from wall import Wall
import slider
from slider import Slider

mouseDown = False

def makeWindow(dimensions):
    screen = pygame.display.set_mode(dimensions)
    pygame.display.set_caption("Particle Party")
    pygame.display.flip()
    return screen

def main():
    mouseDown = False

    pygame.init()
    screen = makeWindow((600, 400))

    maxParticlesSlider = Slider(100, 1, 450, 10, 100, "maxParticles")
    gravityXSlider = Slider(0.5, -0.5, 450, 50, 100, "gravityX")
    gravityXSlider.t = 0.5
    gravityYSlider = Slider(0.5, -0.5, 450, 90, 100, "gravityY")
    gravityYSlider.t = 0.5
    frictionSlider = Slider(1, 0, 450, 130, 100, "friction")
    minSizeSlider = Slider(20, 5, 450, 170, 100, "minSize")
    thetaSlider = Slider(360, 0, 450, 210, 100, "theta")
    velocitySlider = Slider(10, 0.5, 450, 250, 100, "velocity")

    emitter = Emitter(1, 15, 20, 5, 0.15, Particle, [200, 200])

    walls = []
    walls.append(Wall([10, 390], [390, 390], False))
    walls.append(Wall([10, 10], [10, 390], False))
    walls.append(Wall([10, 10], [390, 10], True))
    walls.append(Wall([390, 390], [390, 10], False))
    walls.append(Wall([200, 390], [390, 200], False))

    running = True
    while running:
        screen.fill((0, 0, 0))
        emitter.update(round(maxParticlesSlider.getValue()), round(minSizeSlider.getValue()), round(thetaSlider.getValue()), velocitySlider.getValue())
        for particleI in emitter.particles:
            particleI.update(walls, (gravityXSlider.getValue(), gravityYSlider.getValue()), frictionSlider.getValue())
            pygame.draw.circle(screen, (255, 255, 255), (particleI.position.x, particleI.position.y), particleI.size, 1)
        
        for wallW in walls:
            pygame.draw.line(screen, (255, 255, 255), (wallW.start.x, wallW.start.y), (wallW.end.x, wallW.end.y), 1)
            # pygame.draw.line(screen, (255, 0, 0), (wallW.start.x, wallW.start.y), (wallW.start.x + wallW.normal.x * 10, wallW.start.y + wallW.normal.y * 10), 1)

        maxParticlesSlider.drawSlider(screen)
        gravityXSlider.drawSlider(screen)
        gravityYSlider.drawSlider(screen)
        frictionSlider.drawSlider(screen)
        minSizeSlider.drawSlider(screen)
        thetaSlider.drawSlider(screen)
        velocitySlider.drawSlider(screen)

        if mouseDown:
            pos = pygame.mouse.get_pos()
            maxParticlesSlider.setT(pos[0], pos[1])
            gravityXSlider.setT(pos[0], pos[1])
            gravityYSlider.setT(pos[0], pos[1])
            frictionSlider.setT(pos[0], pos[1])
            minSizeSlider.setT(pos[0], pos[1])
            thetaSlider.setT(pos[0], pos[1])
            velocitySlider.setT(pos[0], pos[1])

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False

        time.sleep(0.0166)
   

if __name__ == "__main__":
    main()
