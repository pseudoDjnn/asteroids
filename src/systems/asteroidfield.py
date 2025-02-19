import pygame
import random
from src.entities import Asteroid
from src.utils import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),  # Moving left from right edge
            lambda y: pygame.Vector2(SCREEN_WIDTH + 2 * ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),  # Moving right from left edge
            lambda y: pygame.Vector2(-2 * ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(0, 1),  # Moving up from bottom edge
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + 2 * ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),  # Moving down from top edge
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -2 * ASTEROID_MAX_RADIUS),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)


            # Adjust position to account for the asteroid radius
            radius = ASTEROID_MIN_RADIUS * kind
            
            if velocity.x > 0 :
                position.x -= radius
                # print(f"Spawning asteroid at position {position}, velocity {velocity}, radius {radius}")
            elif velocity.x < 0:
                position.x += radius
                # print(f"Spawning asteroid at position {position}, velocity {velocity}, radius {radius}")
            if velocity.y > 0 :
                position.y -= radius
                # print(f"Spawning asteroid at position {position}, velocity {velocity}, radius {radius}")
            elif velocity.y < 0:
                position.y += radius
                # print(f"Spawning asteroid at position {position}, velocity {velocity}, radius {radius}")
            

            
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)