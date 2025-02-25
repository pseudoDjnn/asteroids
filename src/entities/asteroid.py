import math
import pygame
import random

from src.entities import CircleShape
from src.utils import ASTEROID_MIN_RADIUS, GAME_STATE, SCREEN_WIDTH, SCREEN_HEIGHT, SMALL_ASTEROID_POINT,MEDIUM_ASTEROID_POINT, LARGE_ASTEROID_POINT

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.num_vertices = random.randint(8, 13)  # Store this as instance variable
    self.offsets = []  # Store the random offsets
    for _ in range(self.num_vertices):
        self.offsets.append(random.uniform(-self.radius * 0.13, self.radius * 0.13))
    self.angle = 0
    self.angle_rotation = random.uniform(-0.5, 0.5)

    
  def draw(self, screen):
    # pygame.draw.circle(screen,"white",self.position,self.radius,2)
        vertices = []
        for i in range(self.num_vertices):
            angle = (2 * math.pi * i / self.num_vertices) + self.angle
            r = self.radius + self.offsets[i]
            x = self.position.x + r * math.cos(angle)
            y = self.position.y + r * math.sin(angle)
            vertices.append((x, y))
        pygame.draw.polygon(screen, "grey", vertices, 2)
    
  def split(self):
    # Increment score based on size:
    if self.radius > ASTEROID_MIN_RADIUS * 2:
      GAME_STATE["score"] += LARGE_ASTEROID_POINT
      # print("Large asteroid destroyed!")
    elif self.radius > ASTEROID_MIN_RADIUS:
      GAME_STATE["score"] += MEDIUM_ASTEROID_POINT
      # print("Medium asteroid destroyed!")
    else:
      GAME_STATE["score"] += SMALL_ASTEROID_POINT
      print("asteroid DESCTRUCTION!")
        
    self.kill() # remove the asteroid from the game
    
    if self.radius <= ASTEROID_MIN_RADIUS:
      # print("this was a small asteroid and we're done")
      return 
    
    random_angle = random.uniform(20, 50)
    
    velocity1 = self.velocity.rotate(random_angle)
    velocity2 = self.velocity.rotate(-random_angle)
    
    new_radius = self.radius / 2
    
    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid1.velocity = velocity1
    
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid2.velocity = velocity2
    
    if hasattr(self, "containers"):
      
      asteroid1.add(self.containers)
      asteroid2.add(self.containers)
      
    # print(f"Asteroid splt into two  smaller asteroids at positions {asteroid1.position} and {asteroid2.position}")
    
  def handle_collision(self, other):
    # Get collision normal
    collision_vector = self.position - other.position
    if collision_vector.length() > 0:
        normal = collision_vector.normalize()
        
        # Swap velocities with some loss of energy
        temp_velocity = self.velocity
        self.velocity = other.velocity 
        other.velocity = temp_velocity 
        
        # Push apart to prevent sticking
        self.position += normal * 1
        other.position -= normal * 1
    
  def update(self, dt):
    
    # Rotate the radius
    self.angle += self.angle_rotation * dt
    
    # Existing movement
    self.position += self.velocity * dt
    
    # Screen wrapping logic
    if self.position.x < 0:
        self.position.x = SCREEN_WIDTH
    elif self.position.x > SCREEN_WIDTH:
        self.position.x = 0

    if self.position.y < 0:
        self.position.y = SCREEN_HEIGHT
    elif self.position.y > SCREEN_HEIGHT:
        self.position.y = 0