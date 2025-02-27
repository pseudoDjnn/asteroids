import pygame

from src.utils import (
  GAME_STATE,
  PLAYER_RADIUS,
  PLAYER_TURN_SPEED,
  PLAYER_SPEED,
  PLAYER_SHOOT_COOLDOWN,
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  MAX_SPEED,
  PLAYER_ACCELERATION,
  ROTATION_ACCELERATION,
  MAX_ROTATION_SPEED
)
from src.entities import CircleShape
from src.entities.shot import Shot

class Player(CircleShape):
  
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    
    self.rotation = 0
    self.shot_timer = 0
    self.velocity = pygame.Vector2(0, 0)
    self.angular_velocity = 0
    
    # Health for player
    self.max_health = 5
    self.health = self.max_health
    self.lives = 3
    # Health bar for player
    self.show_damage_bar = False
    self.damage_bar_timer = 0
    self.damage_bar_alpha = 255
    
    # in the player class
  def triangle(self):
    
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      
      return [a, b, c]
    
  def draw(self, screen):
    
    # This will draw the sprite as normal
    super().draw(screen)
    
    # Update the health bar visibility
    # if GAME_STATE["health"] < 5:
    #   self.show_damage_bar = True
    #   self.damage_bar_timer = 2
    #   self.damage_bar_alpha = 255
      
    # Hand the health bar fade
    if self.show_damage_bar:
      # print("Drawing damage bar")
      self.damage_bar_timer -= 1/60
      
      if self.damage_bar_timer <= 0:
        self.damage_bar_alpha -= 5
        
        if self.damage_bar_alpha <= 0:
          self.show_damage_bar = False
          self. damage_bar_alpha = 255
          return
        
      # Create surface for health bar with transparency
      bar_width = 40
      bar_height = 5
      bar_surface = pygame.Surface((bar_width, bar_height), pygame.SRCALPHA)
      
      # Draw bars with alpha
      health_width = (GAME_STATE["health"] / 5) * bar_width
      red_alpha = (255, 0, 0, self.damage_bar_alpha)
      pygame.draw.rect(bar_surface, red_alpha, (0, 0, health_width, bar_height))

      # Position and draw th ebar surface
      bar_x = self.position.x - bar_width / 2
      bar_y = self.position.y - self.radius - 20
      screen.blit(bar_surface, (bar_x, bar_y))
    
    pygame.draw.polygon(screen, (0, 0, 0, 0), self.triangle(), 0)
    pygame.draw.polygon(screen, "grey", self.triangle(), 2)
      
      
  def rotate(self, dt):
    
    keys = pygame.key.get_pressed()
    # If switching directions, reduce existing angular velocity
    if (keys[pygame.K_a] and self.angular_velocity > 0) or (keys[pygame.K_d] and self.angular_velocity < 0):
        self.angular_velocity *= 0.85  # Helps cancel out opposite momentum faster
    
    self.angular_velocity += ROTATION_ACCELERATION * dt
    self.angular_velocity *= 0.97
    
    if abs(self.angular_velocity) > MAX_ROTATION_SPEED:
        self.angular_velocity = MAX_ROTATION_SPEED * (self.angular_velocity / abs(self.angular_velocity))
    
    self.rotation += self.angular_velocity
    
    
  def move(self, dt):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt
    elif keys[pygame.K_s]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += -forward * PLAYER_ACCELERATION * 0.8 * dt
    
    # Always apply velocity decay (outside the if/elif)
    self.velocity *= 0.987
    
    # Speed limit check
    if self.velocity.length() > MAX_SPEED:
        self.velocity.scale_to_length(MAX_SPEED)
    
    # Update position
    self.position += self.velocity * dt
    
    
  def shoot(self):
    direction = pygame.Vector2(0, 1)
    direction = direction.rotate(self.rotation)
    
    Shot(self.position.x, self.position.y, direction)
    self.shot_timer = PLAYER_SHOOT_COOLDOWN  # Set the cooldown timer
    
    
  def take_damage(self, amount):
    if GAME_STATE["invincible"]:
      return
    
    
    self.health -= amount
    
    if self.health <= 0 :
      self._lose_life()
      
  def _lose_life(self):
      self.lives -= 1
      if self.lives > 0:
        self.respawn()
        GAME_STATE["invincible"] = True
        GAME_STATE["invincible_timer"] = 0
      else:
        self.kill()
    
    
  def respawn(self):
      
    self.position = pygame.math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    self.velocity = pygame.Vector2(0, 0)
    self.rotation = 0
    self.health = self.max_health
    
    
  def update(self, dt):
    keys = pygame.key.get_pressed()
    self.shot_timer -= dt

    if keys[pygame.K_a]:
      self.rotate(-dt * 3)
        
    if keys[pygame.K_d]:
      self.rotate(dt * 3)
        
        
    self.move(dt)
        
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