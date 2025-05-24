
import pygame
from player import Player

from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_start = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        dt = clock.tick(60) / 1000.0
        player_start.update(dt)
        player_start.draw(screen)
        pygame.display.flip()

        


if __name__ == "__main__":
    main()

