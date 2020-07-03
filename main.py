import sys
import settings

import pygame

class Main(object):
    def init(self):
        self.settings = settings
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

    def show(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run(self):
        self.init()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.show()


if __name__ == '__main__':
    main = Main()
    main.run()
