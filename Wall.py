import pygame
from Const import WALL_THICK

class Wall:

    def __init__(self, startPos, endPos):
        self.start = startPos
        self.end = endPos

    def update(self, w):
        pass

    def draw(self, surface):
        pygame.draw.line(surface, "black", self.start, self.end, width=WALL_THICK)

    def rect(self) -> pygame.Rect:
        # FIX THIS when we add vertical walls:
        return pygame.Rect(self.start[0], self.start[1] - WALL_THICK/2, self.end[0] - self.start[0], WALL_THICK)
