import sys

import pygame

import settings
import ship

class Main(object):
    def init(self):
        self.settings = settings
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = ship.Ship(self.screen)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()
        pygame.display.flip()

    def run(self):
        self.init()

        while True:
            self.check_event()
            self.update_screen()

if __name__ == '__main__':
    main = Main()
    main.run()
