import pygame
from pygame.surface import Surface

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print_screen_info()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_queue(screen)


def game_queue(screen: pygame.Surface):
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()


def print_screen_info():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
