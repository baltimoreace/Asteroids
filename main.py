
import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    space_rocks_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (space_rocks_group, updatable, drawable)
    AsteroidField.containers = (updatable,)

    
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_start = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        dt = clock.tick(60) / 1000.0
        updatable.update(dt)
        for asteroid in space_rocks_group:
            if asteroid.collision(player_start):
                print("Game over!")
                sys.exit(0)
            
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        


if __name__ == "__main__":
    main()

