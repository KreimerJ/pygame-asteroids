import pygame

from constants import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print_screen_info()


def print_screen_info():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
