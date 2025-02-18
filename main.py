# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from src.utils.constants import *
from src.entities import Player, Asteroid, Shot
from src.systems import AsteroidField

def main():

    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    time = pygame.time.Clock()
    
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    font = pygame.font.Font(None, 36)
    
    # global SCORE
    
    #Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullets, updatable, drawable)
    
    asteroid_field = AsteroidField()
    
    updatable.add(player)
    drawable.add(player)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        # Prepare score text for display
        score_text = font.render(f"Score: {GAME_STATE["score"]}", True, (225, 255, 255))
        
        # Get the width and height of the text
        text_width = score_text.get_width()
        # text_height = score_text.get_height()
        
        # Calculate top-center for text
        screen_width = screen.get_width()
        x_p = (screen_width // 2) - (text_width // 2)
        y_p = 10
        
        # Draw the score
        screen.blit(score_text, (x_p, y_p))
        
        
        # Prepare lives text for display
        lives_text = font.render(f"Lives: {GAME_STATE["lives"]}", True, (255, 255, 255))
        
        # Get the width o lives
        lives_width = lives_text.get_width()

        # Positioning for the font
        lives_x_p = screen_width - lives_width - 10
        lives_y_p = 10
        
        # Draw the lives
        screen.blit(lives_text, (lives_x_p, lives_y_p))
        
        updatable.update(dt)
        
        # Timer set for being invisible
        if GAME_STATE["invincible"]:
            GAME_STATE["invincible_timer"] -= dt
            if GAME_STATE["invincible_timer"] <= 0:
                GAME_STATE["invincible"] = False
        
        # Collison Detection
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                if not GAME_STATE['invincible']:
                    GAME_STATE["lives"] -= 1
                    if GAME_STATE["lives"] > 0:
                        player.respawn()
                        GAME_STATE["invincible"] = True
                        GAME_STATE["invincible_timer"] = INVINCIBILITY_DURATION
                    else:
                        print("Game Over!")
                        return # exit the program
            
        # Bullet-Asteroid detection
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collides_with(asteroid):
                    print(f"Bullet hit asteroid at {asteroid.position}")
                    bullet.kill()
                    asteroid.split()

        
        for sprite in drawable:
            if sprite == player and GAME_STATE["invincible"]:
                # This is the flash
                if int(GAME_STATE["invincible_timer"]* 13) % 2 == 0:
                    sprite.draw(screen)
            else:
                sprite.draw(screen)   
        
        pygame.display.flip()
        
        dt = time.tick(60) / 1000


if __name__ == "__main__":

    main()