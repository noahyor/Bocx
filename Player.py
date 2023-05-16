import pygame
from Wall import Wall
from Const import GRAVITY, PLAYER_SIZE, WALL_THICK

class Player:

    def __init__(self):
        self.pos = pygame.Vector2(200, 150)
        self.vel = pygame.Vector2(0, 0)

    def update(self, world):
        self.vel += GRAVITY
        self.pos += self.vel

        for wall in world.walls:
            if self.collide(wall):
                self.vel[1] = 0
                self.pos[1] = (wall.start[1] - WALL_THICK / 2) - PLAYER_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, "white", self.rect())

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.pos, (PLAYER_SIZE,PLAYER_SIZE))
    
    def collide(self, w: Wall) -> bool:
        return self.rect().colliderect(w.rect())
