import pygame

from src.utils import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MAX_SPEED,
    PLAYER_ACCELERATION
)
from src.entities import CircleShape
from src.entities.shot import Shot

class Player(CircleShape):
  
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    
    self.rotation = 0
    self.shot_timer = 0
    self.velocity = pygame.Vector2(0, 0)
    
    # in the player class
  def triangle(self):
    
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      
      return [a, b, c]
    
  def draw(self, screen):
    
      pygame.draw.polygon(screen, "white", self.triangle(), 2)
      
      
  def rotate(self, dt):
    
    self.rotation += PLAYER_TURN_SPEED * dt
    
    
  def move(self, dt):
    # Get direction vector based on rotation
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        # Forward thrust
        self.velocity += forward * PLAYER_ACCELERATION
    elif keys[pygame.K_s]:
        # Reverse thrust (half speed)
        self.velocity = -forward * -PLAYER_ACCELERATION * 0.5
    else:
        # Slowdown when not thrusting
        self.velocity *= 0.9999995
        
        # Optional: Add after velocity changes
    if self.velocity.length() > MAX_SPEED:
        self.velocity.scale_to_length(MAX_SPEED)
    
    # Update position
    self.position += self.velocity * dt
    
    
  def shoot(self):
    # print("Shooting!")
    direction = pygame.Vector2(0, 1)
    
    direction = direction.rotate(self.rotation)
    
    Shot(self.position.x, self.position.y, direction)
    
    self.shot_timer = PLAYER_SHOOT_COOLDOWN  # Set the cooldown timer
    
    
  def respawn(self):
      
    self.position = pygame.math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    self.velocity = pygame.Vector2(0, 0)
    self.rotation = 0
    
    
  def update(self, dt):
    keys = pygame.key.get_pressed()
    
    self.shot_timer -= dt

    if keys[pygame.K_a]:
      
      self.rotate(-dt)
        
    if keys[pygame.K_d]:
      
      self.rotate(dt)
        
    if keys[pygame.K_w]:

      self.move(dt)
        
    if keys[pygame.K_s]:

      self.move(-dt)
        
    if keys[pygame.K_SPACE]:
      
      if self.shot_timer <= 0:
        self.shoot()
        
    if self.position.x < 0:
      self.position.x = SCREEN_WIDTH
    elif self.position.x > SCREEN_WIDTH:
      self.position.x = 0
      
    if self.position.y < 0:
      self.position.y = SCREEN_HEIGHT
    elif self.position.y > SCREEN_HEIGHT:
      self.position.y = 0