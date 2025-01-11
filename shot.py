from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0) # Start with zero velocity
    
    def update(self, dt):
        # Update x position
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius)