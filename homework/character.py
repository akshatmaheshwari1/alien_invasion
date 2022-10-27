import pygame
import time

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0, 0, 255))

#draw the character
character = pygame.image.load('../images/plane.png')
character_rect = character.get_rect()
screen_rect = screen.get_rect()
character_rect.center = screen_rect.center

screen.blit(character, character_rect)

pygame.display.flip()

time.sleep(4)