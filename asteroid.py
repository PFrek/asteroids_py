import pygame
import random
from circleshape import CircleShape
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_MIN_LUMPNESS,
    ASTEROID_MAX_LUMPNESS,
    SHOW_HITBOX,
)


def lumpify(val):
    return random.uniform(ASTEROID_MIN_LUMPNESS, ASTEROID_MAX_LUMPNESS) * val


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.lump_factors = [1] * 8

        self.lump_factors = list(map(lumpify, self.lump_factors))

    def draw(self, screen):
        if SHOW_HITBOX:
            super().draw(screen)

        vertices = [
            pygame.Vector2(self.position.x, self.position.y - self.radius),
            # TOP RIGHT
            pygame.Vector2(
                self.position.x + self.radius * self.lump_factors[0],
                self.position.y - self.radius * 0.8,
            ),
            pygame.Vector2(
                self.position.x + self.radius * 0.8,
                self.position.y - self.radius * self.lump_factors[1],
            ),
            pygame.Vector2(self.position.x + self.radius, self.position.y),
            # BOTTOM RIGHT
            pygame.Vector2(
                self.position.x + self.radius * 0.8,
                self.position.y + self.radius * self.lump_factors[2],
            ),
            pygame.Vector2(
                self.position.x + self.radius * self.lump_factors[3],
                self.position.y + self.radius * 0.8,
            ),
            pygame.Vector2(self.position.x, self.position.y + self.radius),
            # BOTTOM LEFT
            pygame.Vector2(
                self.position.x - self.radius * self.lump_factors[4],
                self.position.y + self.radius * 0.8,
            ),
            pygame.Vector2(
                self.position.x - self.radius * 0.8,
                self.position.y + self.radius * self.lump_factors[5],
            ),
            pygame.Vector2(self.position.x - self.radius, self.position.y),
            # TOP LEFT
            pygame.Vector2(
                self.position.x - self.radius * 0.8,
                self.position.y - self.radius * self.lump_factors[6],
            ),
            pygame.Vector2(
                self.position.x - self.radius * self.lump_factors[7],
                self.position.y - self.radius * 0.8,
            ),
        ]

        pygame.draw.polygon(screen, "white", vertices, 2)
        # pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        velocity_a = self.velocity.rotate(angle)
        velocity_b = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = velocity_a * 1.2

        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = velocity_b * 1.2
