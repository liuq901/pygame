import sys

import pygame

import settings
import ship

class Main(object):
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = ship.Ship(self.screen)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move(1)
                elif event.key == pygame.K_LEFT:
                    self.ship.move(-1)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move(-1)
                elif event.key == pygame.K_LEFT:
                    self.ship.move(1)

    def update_screen(self):
        self.screen.fill(settings.bg_color)
        self.ship.blit()
        pygame.display.flip()

    def run(self):
        self.init()

        while True:
            self.check_event()
            self.ship.update_position()
            self.update_screen()

if __name__ == '__main__':
    main = Main()
    main.run()
