import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0, 0, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_RIGHT:
                print("moving right")
            elif event.key == pygame.K_LEFT:
                print("moving left")
            elif event.key == pygame.K_UP:
                print("moving up")
            elif event.key == pygame.K_DOWN:
                print("moving down")



