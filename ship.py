import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom

    def blit(self):
        self.screen.blit(self.image, self.rect)
