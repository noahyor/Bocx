import pygame, sys
from Player import *
from pygame.locals import QUIT
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Bocx')
clock = pygame.time.Clock()

things = [Player()]

def update():
    for thing in things:
        thing.update()

def draw():
    DISPLAYSURF.fill("black")
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
