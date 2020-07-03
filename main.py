import sys

import pygame

class Main(object):
    def init(self):
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run(self):
        self.init()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()
