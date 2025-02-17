# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_STATE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
        
        updatable.update(dt)
        
        # Collison Detection
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                return # exit the program
            
        # Bullet-Asteroid detection
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collides_with(asteroid):
                    print(f"Bullet hit asteroid at {asteroid.position}")
                    bullet.kill()
                    asteroid.split()
                    # SCORE += 10
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        dt = time.tick(60) / 1000


if __name__ == "__main__":

    main()