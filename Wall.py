import pygame


class Wall:

    def __init__(self, startPos, endPos):
        self.start = startPos
        self.end = endPos

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.line(surface, "black", self.start, self.end, width=20)
