import pygame
import random
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT,STAR_COUNT, STAR_MIN_SPEED, STAR_MAX_SPEED
from src.entities import CircleShape


class Star(CircleShape):
  def __init__(self, x, y, radius, speed):
    super().__init__(x, y, radius,)


class Starfield():
  def __init__(self, radius):
    self.stars = []
    
    for i in range(STAR_COUNT):
      x = random.randint(0, SCREEN_WIDTH)
      y = random.randint(0, SCREEN_HEIGHT)
      speed = random.randint(STAR_MIN_SPEED, STAR_MAX_SPEED)
      new_star = Star(x, y, radius, speed)
      self.stars.append(new_star)
    
  def draw(self, screen):
    for star in self.stars:
      pygame.draw.circle(screen, "grey", star.position, star.radius)
  
  def update(self, dt):
    for star in self.stars:
      pass