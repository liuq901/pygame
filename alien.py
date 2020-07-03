import pygame

import settings

class Alien(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.movement = 1

    def touch_edge(self):
        return self.rect.right > self.screen.get_rect().right or self.rect.left < 0

    def update(self):
        self.x += self.movement * settings.alien_speed
        self.rect.x = int(self.x)
