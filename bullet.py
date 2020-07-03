import pygame

import settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ship):
        super(Bullet, self).__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def update(self):
        self.y -= settings.bullet_speed
        self.rect.y = int(self.y)

    def draw(self):
        pygame.draw.rect(self.screen, settings.bullet_color, self.rect)
