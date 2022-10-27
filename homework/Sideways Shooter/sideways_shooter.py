import pygame
import sys
from bullet import Bullet

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

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()
            self.update()
            self._update_bullets()

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
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.rect.y = self.y

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.screen.blit(self.character, self.rect)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

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

if __name__ == '__main__':
    test = Sideways_Shooter()
    test.run_game()