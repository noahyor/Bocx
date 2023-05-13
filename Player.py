import pygame


class Player:

    def __init__(self):
        self.pos = pygame.Vector2(200, 150)
        self.vel = pygame.Vector2(0, 0)
        self.fric = 2

    def update(self):
        self.pos += self.vel
        try:
            self.vel -= (self.vel / ((5 - self.fric) ** 2))
        except ZeroDivisionError:
            pass
    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.pos, (50, 50)))
