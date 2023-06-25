# TODO: Use sprites instead of manually rendering

import pygame, sys
from World import World
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP
from Const import JUMP_VEL, LR_ACCEL

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Bocx')
clock = pygame.time.Clock()

world = World()

left = False
right = False

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
                world.PLAYER.vel += pygame.Vector2(0, -JUMP_VEL)
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            elif event.key == K_RIGHT:
                right = False

    if left:
        world.PLAYER.vel += pygame.Vector2(-LR_ACCEL, 0)

    if right:
        world.PLAYER.vel += pygame.Vector2(LR_ACCEL, 0)

    world.update()
    world.draw(DISPLAYSURF)
    pygame.display.update()

    clock.tick(60)
