import pygame
import sys
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('../images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
class Stars:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.screen.fill((230, 230, 230))

        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        star = Star(self)

        star_width, star_height = star.rect.size
        available_space_x = 600 - (2* star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = 600 - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)


    def _create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x + randint(-20,20)
        star.rect.y = star_height + 2*star.rect.height * row_number + randint(-20,20)
        self.stars.add(star)

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = Stars()
    ai.run_game()

