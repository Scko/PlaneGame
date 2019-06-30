import pygame
from pygame.locals import *

width, height = 640, 400


class Game:

    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.plane = Triangle()
        self.bullets = []
        self.background = pygame.image.load("trees.jpg")

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.running = True

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                self.plane.ypos -= 10
            if event.key == pygame.K_DOWN:
                self.plane.ypos += 10
            if event.key == pygame.K_LEFT:
                self.plane.xpos -= 10
            if event.key == pygame.K_RIGHT:
                self.plane.xpos += 10
            if event.key == pygame.K_SPACE:
                self.bullets.append(Bullet(self.plane.xpos+self.plane.frontandcenter, self.plane.ypos))

    def loop(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.plane.image, (self.plane.xpos, self.plane.ypos))
        for bullet in self.bullets:
            bullet.ypos += bullet.step_y
            self.screen.blit(bullet.image, (bullet.xpos, bullet.ypos))

    def render(self):
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def run(self):
        if self.initialize():
            self.running = False

        pygame.key.set_repeat(50, 50)
        while self.running:
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()


class Triangle:

    def __init__(self):
        self.image = pygame.image.load("triangle.png")
        self.xpos = 50
        self.ypos = 50
        self.step_x = 10
        self.step_y = 10
        self.frontandcenter = 25

class Bullet:

    def __init__(self, xpos, ypos):
        self.image = pygame.image.load("bullet.png")
        self.xpos = xpos
        self.ypos = ypos
        self.step_x = 0
        self.step_y = -1

if __name__ == "__main__":
    game = Game()
    game.run()
