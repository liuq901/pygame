import pygame

import settings

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Ship, self).__init__()

        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom

        self.center = float(self.rect.centerx)

        self.movement = 0

    def move(self, direction):
        self.movement += direction

    def update(self):
        bakcup = (self.center, self.rect)

        self.center += self.movement * settings.ship_speed
        self.rect.centerx = int(self.center)

        if self.rect.left < 0 or self.rect.right > self.screen.get_rect().right:
            self.center, self.rect = bakcup

    def draw(self):
        self.screen.blit(self.image, self.rect)
