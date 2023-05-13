# TODO: Use sprites instead of manually rendering

import pygame, sys
from Player import Player
from Wall import Wall
from pygame.locals import QUIT
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Bocx')
clock = pygame.time.Clock()

things = [Player(), Wall((0, 250),(250, 200))]

def update():
    for thing in things:
        thing.update()

def draw():
    DISPLAYSURF.fill("grey")
    for thing in things:
        thing.draw(DISPLAYSURF)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    update()
    draw()
    pygame.display.update()

    clock.tick(60)
