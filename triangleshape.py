import pygame
from constants import PLAYER_RADIUS


class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * PLAYER_RADIUS / 1.5
        a = self.position + forward * PLAYER_RADIUS
        b = self.position - forward * PLAYER_RADIUS - right
        c = self.position - forward * PLAYER_RADIUS + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.triangle())
        pass

    def update(self, dt):
        pass
