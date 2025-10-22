import circleshape
import pygame
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        p = pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
