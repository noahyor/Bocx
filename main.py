# TODO: Use sprites instead of manually rendering

import pygame, sys
from Player import Player
from Wall import Wall
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Bocx')
clock = pygame.time.Clock()

PLAYER = Player()
things = [PLAYER, Wall((0, 250), (250, 200))]


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
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                PLAYER.vel = pygame.Vector2(-1, 0)
            elif event.key == K_RIGHT:
                PLAYER.vel = pygame.Vector2(1, 0)
        elif event.type == KEYUP:
            PLAYER.vel = pygame.Vector2(0, 0)
    update()
    draw()
    pygame.display.update()

    clock.tick(60)
