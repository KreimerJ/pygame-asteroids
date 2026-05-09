import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_half_angle = self.velocity.rotate(angle)
        second_half_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_half_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_half_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_half_asteroid.velocity = first_half_angle * 1.2
        second_half_asteroid.velocity = second_half_angle * 1.2
