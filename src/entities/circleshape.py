import pygame

from src.entities.player import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius):

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def draw(self, screen):
        # sub-classes must override
        pass

    def collides_with(self, other):
        # collision detection
        # pass
        distance = self.position.distance_to(other.position)
        
        if distance < (self.radius + other.radius):
            return True
        return False

    def update(self, dt):
        # sub-classes must override
        pass
    