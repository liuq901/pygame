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
