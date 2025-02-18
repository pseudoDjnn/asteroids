import pygame

from src.entities.circleshape import CircleShape
from src.utils.constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
  def __init__(self, x, y ,direction):
    super().__init__(x, y,SHOT_RADIUS)
    
    self.velocity = direction * PLAYER_SHOOT_SPEED
    
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius)
    
  def update(self, dt):
    self.position += self.velocity * dt