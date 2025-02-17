import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self,screen):
    pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
  def update(self, dt):
    self.position += self.velocity * dt
    
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      print("this was a small asteroid and we're done")
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
      
    print(f"Asteroid splt into two  smaller asteroids at positions {asteroid1.position} and {asteroid2.position}")