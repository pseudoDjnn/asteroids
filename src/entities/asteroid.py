import pygame
import random

from src.entities import CircleShape
from src.utils import ASTEROID_MIN_RADIUS, GAME_STATE, SCREEN_WIDTH, SCREEN_HEIGHT, SMALL_ASTEROID_POINT,MEDIUM_ASTEROID_POINT, LARGE_ASTEROID_POINT

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self,screen):
    pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
  def split(self):
    
    global SCORE
    
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
    
  def update(self, dt):
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