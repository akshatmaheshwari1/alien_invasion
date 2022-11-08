import pygame
import sys
from bullet import Bullet
from alien import Alien
from random import randint
import time

class Sideways_Shooter:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.screen.fill((230, 230, 230))
        # draw the character
        self.character = pygame.image.load('../../images/shiprotated.bmp')
        self.rect = self.character.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

        self.y = float(self.rect.y)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.lives = 5
        self.game_active = True



    def run_game(self):
        while True:
            if self.game_active:
                clock = pygame.time.Clock()
                self._update_screen()
                self._check_events()
                self.update()
                self._update_bullets()
                self.create_aliens()
                self.update_aliens()
                clock.tick(60)
            else:
                print("GAME OVER, YOU LOSE!")
                break

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                self.moving_up = False
                self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= 10
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 10

        self.rect.y = self.y



    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.screen.blit(self.character, self.rect)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < 5:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)

        self.check_bullet_collisions()
    def create_aliens(self):
        if len(self.aliens) < 3:
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = 600
            alien.rect.x = alien.x
            alien.rect.y = randint(0, 600 - alien_height)
            self.aliens.add(alien)

    def update_aliens(self):
        self.aliens.update()
        for alien in self.aliens:
            if alien.rect.colliderect(self.rect):
                self.aliens.remove(alien)
                self.ship_hit()
            if alien.rect.left <= 0:
                self.aliens.remove(alien)
                self.lives -= 1
                if self.lives < 1:
                    self.game_active = False

    def check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
    def ship_hit(self):
        if self.lives > 1:
            self.lives -= 1
            self.rect.midleft = self.screen_rect.midleft
            time.sleep(1)
        else:
            self.game_active = False

if __name__ == '__main__':
    test = Sideways_Shooter()
    test.run_game()