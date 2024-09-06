import pygame
from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x=x, y=y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt
        return self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(
                self.position.x, self.position.y, new_radius
            )
            new_asteroid2 = Asteroid(
                self.position.x, self.position.y, new_radius
            )
            new_asteroid.velocity = vector
            new_asteroid2.velocity = vector2
