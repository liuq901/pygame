import pygame

import settings

class Button(object):
    def __init__(self, screen, msg):
        self.screen = screen

        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, settings.button_width, settings.button_height)
        self.rect.center = self.screen.get_rect().center

        self.image = self.font.render(msg, True, settings.button_text_color, settings.button_color)
        self.msg_rect = self.image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(settings.button_color, self.rect)
        self.screen.blit(self.image, self.msg_rect)
