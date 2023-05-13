import pygame


class Player:

    def __init__(self):
        self.pos = pygame.Vector2(200, 150)
        self.vel = pygame.Vector2(0, 0)

    def update(self):
        self.pos += self.vel
        self.vel -= (self.vel / 32)

    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.pos, (50, 50)))
