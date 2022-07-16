import pygame, sys
from settings import *
from tiles import Tile
from level import Level


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Battle of Bassam')
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    screen.fill('white')
    level.run()

    pygame.display.update()
    clock.tick(30)
