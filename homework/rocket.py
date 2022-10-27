import pygame
import sys
class Rocket:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        self.screen.fill((230, 230, 230))
        # draw the character
        self.character = pygame.image.load('../images/ship.bmp')
        self.rect = self.character.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def run_game(self):
        while True:
            self._check_events()
            self.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_q:
                    sys.exit
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
                elif event.key == pygame.K_UP:
                    self.moving_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False
                elif event.key == pygame.K_UP:
                    self.moving_up = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0 :
            self.x -= 1
        self.rect.x = self.x

        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1
        self.rect.y = self.y

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.screen.blit(self.character, self.rect)
        pygame.display.flip()

if __name__ == '__main__':
    test = Rocket()
    test.run_game()
