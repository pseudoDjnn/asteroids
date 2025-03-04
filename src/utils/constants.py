SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

GAME_STATE = {
  "score": 0,
  "health": 5,
  "lives": 3,
  "invincible": False,
  "invincible_timer": 0

}

INVINCIBILITY_DURATION = 3.0
SMALL_ASTEROID_POINT = 5
MEDIUM_ASTEROID_POINT = 10
LARGE_ASTEROID_POINT = 20

STAR_COUNT = 100
STAR_MIN_SIZE = 1
STAR_MAX_SIZE = 3
STAR_MIN_SPEED = 8
STAR_MAX_SPEED = 55

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 5.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 233

PLAYER_ACCELERATION = 610
ROTATION_ACCELERATION = 13
MAX_SPEED = 377
MAX_ROTATION_SPEED = 8


DRAG_COEFFICIENT = 0.99

SHOT_RADIUS = 3
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3