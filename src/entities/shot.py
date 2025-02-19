import pygame

from src.entities import CircleShape
from src.utils import SCREEN_HEIGHT,SCREEN_WIDTH, SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
  def __init__(self, x, y ,direction):
    super().__init__(x, y,SHOT_RADIUS)
    
    self.velocity = direction * PLAYER_SHOOT_SPEED
    
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius)
    
  def update(self, dt):
    self.position += self.velocity * dt
    
    # Inside Shot's update method
    if self.position.x < 0 or self.position.x > SCREEN_WIDTH or self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
      self.kill()