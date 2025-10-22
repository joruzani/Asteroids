import circleshape
import pygame
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        p = pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
