import pygame
from Wall import Wall
from Const import GRAVITY

class Player:

    def __init__(self):
        self.pos = pygame.Vector2(200, 150)
        self.vel = pygame.Vector2(0, 0)

    def update(self):
        self.vel += GRAVITY
        self.pos += self.vel

    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.pos, (50, 50)))

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.pos, (50,50))
    
    def collide(self, w: Wall) -> bool:
        return self.rect().colliderect(w.rect())
