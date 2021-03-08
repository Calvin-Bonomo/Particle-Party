import pygame

class Slider:
    def __init__(self, maxValue, minValue, xpos, ypos, width, title):
        self.maxValue = maxValue - minValue
        self.minValue = minValue
        self.t = 0

        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.title = title
    
    def setT(self, mouseX, mouseY):
        if (mouseX <= self.xpos + self.width and mouseX >= self.xpos and mouseY >= self.ypos + 20 and mouseY <= self.ypos + 40):
            mouseX -= self.xpos
            self.t = mouseX/self.width
    
    def getSliderX(self):
        return self.xpos + self.width * self.t

    def getValue(self):
        return self.t * self.maxValue + self.minValue
    
    def drawSlider(self, screen):
        font = pygame.font.SysFont(None, 24)
        img = font.render(self.title + ": " + str(self.getValue()), True, (255, 255, 255))
        screen.blit(img, (self.xpos, self.ypos))

        pygame.draw.line(screen, (160, 160, 160), (self.xpos, self.ypos + 30), (self.xpos + self.width, self.ypos + 30), 5)
        pygame.draw.circle(screen, (255, 0, 0), (self.getSliderX(), self.ypos + 30), 10, 5)