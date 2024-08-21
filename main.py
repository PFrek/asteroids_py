import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    num_init, num_fail = pygame.init()
    print(f"Pygame initialization: success ({
          num_init}) | failure ({num_fail})")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color("black"))
        pygame.display.flip()


if __name__ == "__main__":
    main()
