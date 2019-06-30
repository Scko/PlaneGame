import pygame


width, height = 640, 400


class Game:

    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.title = "Plane Shooty"
        self.clock = pygame.time.Clock()
        self.plane = Triangle()
        self.bullets = []
        self.background = pygame.image.load("trees.jpg")

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        pygame.display.set_caption(self.title)
        self.running = True

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.plane.ypos -= self.plane.speed
        if keys[pygame.K_DOWN]:
            self.plane.ypos += self.plane.speed
        if keys[pygame.K_LEFT]:
            self.plane.xpos -= self.plane.speed
            self.plane.goingLeft = True
            self.plane.goingRight = False
        elif keys[pygame.K_RIGHT]:
            self.plane.xpos += self.plane.speed
            self.plane.goingLeft = False
            self.plane.goingRight = True
        else:
            self.plane.goingLeft = False
            self.plane.goingRight = False
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.plane.xpos+self.plane.frontandcenter, self.plane.ypos))

    def loop(self):
        for bullet in self.bullets:
            bullet.ypos -= bullet.speed

    def render(self):
        self.screen.blit(self.background, (0, 0))
        if not self.plane.goingLeft and not self.plane.goingRight:
            self.screen.blit(self.plane.images[0], (self.plane.xpos, self.plane.ypos))
        elif self.plane.goingLeft:
            self.screen.blit(self.plane.images[1], (self.plane.xpos, self.plane.ypos))
        elif self.plane.goingRight:
            self.screen.blit(self.plane.images[3], (self.plane.xpos, self.plane.ypos))
        for bullet in self.bullets:
            self.screen.blit(bullet.image, (bullet.xpos, bullet.ypos))
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def run(self):
        if self.initialize():
            self.running = False

        pygame.key.set_repeat(30, 30)
        while self.running:
            self.clock.tick(30)

            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()


class Triangle:

    def __init__(self):
        self.images = [pygame.image.load("l0_Plane1.png"), pygame.image.load("l0_Plane2.png"),
                       pygame.image.load("l0_Plane3.png"), pygame.image.load("l0_Plane4.png")]
        self.currentImage = 0
        self.goingLeft = False
        self.goingRight = False
        self.xpos = 50
        self.ypos = 50
        self.speed = 10
        self.frontandcenter = 25

class Bullet:

    def __init__(self, xpos, ypos):
        self.image = pygame.image.load("bullet.png")
        self.xpos = xpos
        self.ypos = ypos
        self.speed = 5

if __name__ == "__main__":
    game = Game()
    game.run()
