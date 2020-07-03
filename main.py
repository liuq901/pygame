import sys

import pygame

import settings
import ship
import bullet

class Main(object):
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = ship.Ship(self.screen)
        self.bullets = pygame.sprite.Group()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move(1)
                elif event.key == pygame.K_LEFT:
                    self.ship.move(-1)
                elif event.key == pygame.K_SPACE:
                    if len(self.bullets) < settings.bullet_limit:
                        self.bullets.add(bullet.Bullet(self.screen, self.ship))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move(-1)
                elif event.key == pygame.K_LEFT:
                    self.ship.move(1)

    def update(self):
        self.ship.update()
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.fill(settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets:
            bullet.draw()
        pygame.display.flip()

    def run(self):
        self.init()

        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == '__main__':
    main = Main()
    main.run()
