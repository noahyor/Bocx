# TODO: Use sprites instead of manually rendering

import pygame, sys
from Player import Player
from Wall import Wall
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Bocx')
clock = pygame.time.Clock()

PLAYER = Player()
# Just in case:
# WALL = Wall((0, 250), (250, 200))
# things = [PLAYER, WALL]
things = [PLAYER, Wall((0, 289), (400, 289))]

left = False
right = False
up = False
down = False

speed = 0.05
fric = 5
# Max Friction: 5
PLAYER.fric = fric


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
                left = True
            elif event.key == K_RIGHT:
                right = True
            elif event.key == K_UP:
                up = True
            elif event.key == K_DOWN:
                down = True
            #if event.key == K_LEFT:
            #    PLAYER.vel = pygame.Vector2(-1, 0)
            #elif event.key == K_RIGHT:
            #    PLAYER.vel = pygame.Vector2(1, 0)
            #elif event.key == K_UP:
            #    PLAYER.vel = pygame.Vector2(0, -1)
            #elif event.key == K_DOWN:
            #    PLAYER.vel = pygame.Vector2(0, 1)
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            elif event.key == K_RIGHT:
                right = False
            elif event.key == K_UP:
                up = False
            elif event.key == K_DOWN:
                down = False

    if left:
        PLAYER.vel += pygame.Vector2(-speed, 0)

    if right:
        PLAYER.vel += pygame.Vector2(speed, 0)

    if up:
        PLAYER.vel += pygame.Vector2(0, -speed)

    if down:
        PLAYER.vel += pygame.Vector2(0, speed)

    update()
    draw()
    pygame.display.update()

    clock.tick(60)
