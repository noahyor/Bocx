import pygame

class Player:

    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x += 1
        self.y += 1

    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.x, self.y, 50, 50))