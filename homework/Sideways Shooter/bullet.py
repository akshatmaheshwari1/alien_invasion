import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60,60,60)

        self.rect = pygame.Rect(0,0, 7, 3)
        self.rect.midtop = ai_game.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += 0.25
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, (60,60,60), self.rect)
