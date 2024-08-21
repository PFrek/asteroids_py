import pygame
from helpers import triangle_vs_circle
from triangleshape import TriangleShape


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other):
        if isinstance(other, CircleShape):
            distance = self.position.distance_to(other.position)

            return distance < self.radius + other.radius

        if isinstance(other, TriangleShape):
            a, b, c = other.triangle()

            return triangle_vs_circle(
                a.x,
                a.y,
                b.x,
                b.y,
                c.x,
                c.y,
                self.position.x,
                self.position.y,
                self.radius,
            )

        return False

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)
        pass

    def update(self, dt):
        pass
