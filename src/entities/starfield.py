import pygame
import random
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities import CircleShape


class Star(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)


class Starfield():
  def __init__(self, radius):
    self.stars = []
    
    for i in range(10):
      x = random.randint(0, SCREEN_WIDTH)
      y = random.randint(0, SCREEN_HEIGHT)
      new_star = Star(x, y, radius)
      self.stars.append(new_star)
    # return self.stars
    
  def draw(self, screen):
    # pass
    for star in self.stars:
      pygame.draw.circle(screen, "grey", star.position, star.radius)
  
  def update(self, dt):
    pass