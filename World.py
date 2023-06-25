import pygame
from Wall import Wall
from Player import Player

class World:
    def __init__(self):
        
        self.PLAYER = Player()
        self.WALL = Wall((0, 250), (250, 250))
        self.walls = [self.WALL]
        self.things = [self.PLAYER, self.WALL]
        # Just in case:
        # things = [PLAYER, Wall((0, 289), (400, 289))]

    def update(self):
        for thing in self.things:
            thing.update(self)

    def draw(self, surf):
        surf.fill("grey")
        for thing in self.things:
            thing.draw(surf)



