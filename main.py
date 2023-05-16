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
WALL = Wall((0, 250), (250, 250))
things = [PLAYER, WALL]
# things = [PLAYER, Wall((0, 289), (400, 289))]

left = False
right = False
up = False
down = False
colliding = False

speed = 0.05

def update():
    for thing in things:
        thing.update()


def draw():
    DISPLAYSURF.fill("grey" if colliding else "blue")
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

    colliding = PLAYER.collide(WALL)
    
    update()
    draw()
    pygame.display.update()

    clock.tick(60)
