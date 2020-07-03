import sys

import pygame

import settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class Main(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

    def creat_enemy(self):
        origin = Alien(self.screen)
        width = origin.rect.width
        height = origin.rect.height
    
        y = origin.rect.y
        for i in xrange(settings.alien_row_number):
            x = origin.rect.x
            for j in xrange(settings.alien_col_number):
                alien = Alien(self.screen)
                alien.rect.x = x
                alien.rect.y = y
                x += width * 2
                self.aliens.add(alien)
            y += height * 2

    def init(self):
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.creat_enemy()

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
                        self.bullets.add(Bullet(self.screen, self.ship))
                elif event.key == pygame.K_q:
                    sys.exit()
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
        self.aliens.draw(self.screen)
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
