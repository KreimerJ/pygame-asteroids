import sys

import pygame
from pygame.surface import Surface

from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import HALF_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print_screen_info()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / HALF_SIZE, SCREEN_HEIGHT / HALF_SIZE)
    asteroid_field = AsteroidField()

    game_queue(screen, clock, updatable, drawable, asteroids, player)


def game_queue(
    screen: Surface,
    clock: pygame.time.Clock,
    updatable: pygame.sprite.Group,
    drawable: pygame.sprite.Group,
    asteroid_group: pygame.sprite.Group,
    player: Player,
):
    dt = 0
    asteroids = asteroid_group
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updatable.update(dt)

        detect_collisions(asteroid_group, player, screen)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        clock_dt = clock.tick(60)
        dt = clock_dt / 1000


def detect_collisions(
    asteroids: pygame.sprite.Group, player: Player, screen: pygame.Surface
):
    for asteroid in asteroids:
        if asteroid.collides_with(player):
            log_event("player_hit")
            print("game over")
            game_over_message(screen)
            pygame.time.wait(3000)
            sys.exit()


def game_over_message(screen: pygame.Surface):
    font = pygame.font.SysFont(None, 64)

    # 2. Render the text into an image. (True = anti-aliasing/smooth edges, "white" = color)
    text_surface = font.render(
        "You lost your ship, you cannot continue.", True, "white"
    )

    # 3. Figure out where the exact middle of the screen is
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # 4. "Blit" (paste) the text image onto your main screen
    screen.blit(text_surface, text_rect)

    # 5. Force the screen to update right now so we actually see it
    pygame.display.flip()


def print_screen_info():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
