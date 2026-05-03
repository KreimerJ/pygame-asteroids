import pygame
from pygame.surface import Surface

from circleshape import CircleShape
from constants import HALF_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print_screen_info()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / HALF_SIZE, SCREEN_HEIGHT / HALF_SIZE)

    game_queue(screen, clock, player)


def game_queue(screen: Surface, clock: pygame.time.Clock, player: Player):
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
        clock_dt = clock.tick(60)
        dt = clock_dt / 1000


def print_screen_info():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
