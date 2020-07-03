import sys
import time

import pygame

import settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class Main(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.game_start = False

    def creat_enemy(self):
        origin = Alien(self.screen)
        width = origin.rect.width
        height = origin.rect.height
    
        y = origin.rect.y
        for i in xrange(settings.alien_row_number):
            x = origin.rect.x
            for j in xrange(settings.alien_col_number):
                alien = Alien(self.screen)
                alien.rect.x = x
                alien.rect.y = y
                alien.x = float(x)
                x += width * 2
                self.aliens.add(alien)
            y += height * 2

    def init(self):
        settings.init()
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.button = Button(self.screen, 'Play')

        self.creat_enemy()

        self.ship_left = settings.ship_limit

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move(1)
                elif event.key == pygame.K_LEFT:
                    self.ship.move(-1)
                elif event.key == pygame.K_SPACE:
                    if len(self.bullets) < settings.bullet_limit:
                        self.bullets.add(Bullet(self.screen, self.ship))
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move(-1)
                elif event.key == pygame.K_LEFT:
                    self.ship.move(1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if not self.game_start and self.button.rect.collidepoint(x, y):
                    self.game_start = True
                    pygame.mouse.set_visible(False)
                    self.init()

    def remove_outside_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def check_collision(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(self.aliens) == 0:
            self.bullets.empty()
            self.creat_enemy()
            settings.level_up()

    def aliens_touch_edge(self):
        for alien in self.aliens:
            if alien.touch_edge():
                return True
        return False

    def change_aliens_direction(self):
        for alien in self.aliens:
            alien.rect.y += settings.alien_drop_speed
            alien.movement *= -1

    def gameover(self):
        if self.ship_left > 0:
            self.ship_left -= 1
            self.ship.init()
            self.bullets.empty()
            self.aliens.empty()
            self.creat_enemy()
            time.sleep(0.5)
        else:
            self.game_start = False
            pygame.mouse.set_visible(True)

    def check_gameover(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.gameover()
        for alien in self.aliens:
            if alien.rect.bottom > self.screen.get_rect().bottom:
                self.gameover()
                break

    def update(self):
        self.ship.update()

        self.bullets.update()
        self.remove_outside_bullet()
        self.check_collision()

        if self.aliens_touch_edge():
            self.change_aliens_direction()
        self.aliens.update()

        self.check_gameover()

    def draw(self):
        self.screen.fill(settings.bg_color)
        if self.game_start:
            self.ship.draw()
            for bullet in self.bullets:
                bullet.draw()
            self.aliens.draw(self.screen)
        else:
            self.button.draw()
        pygame.display.flip()

    def run(self):
        self.init()

        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == '__main__':
    main = Main()
    main.run()
