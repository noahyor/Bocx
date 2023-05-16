import pygame


class Wall:

    def __init__(self, startPos, endPos):
        self.start = startPos
        self.end = endPos

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.line(surface, "black", self.start, self.end, width=20)

    def rect(self) -> pygame.Rect:
        # FIX THIS when we add vertical walls
        return pygame.Rect(self.start[0], self.start[1] - 10, self.end[0] - self.start[0], 20)
