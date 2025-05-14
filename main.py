# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player

from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    myCounter = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create Groups before Player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    print(f"Spawning Player at: ({x}, {y})")
    newPlayer = Player(x, y)

    #newPlayer.containers = (updatable, drawable)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        #newPlayer.draw(screen)
        #newPlayer.update(dt)

        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = myCounter.tick(60) / 1000

if __name__ == "__main__":
    main()
