import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_left = Asteroid(self.position.x, self.position.y, radius)
        velocity_left = self.velocity.rotate(angle * -1)
        asteroid_left.velocity = velocity_left * 1.2

        asteroid_right = Asteroid(self.position.x, self.position.y, radius)
        velocity_right = self.velocity.rotate(angle)
        asteroid_right.velocity = velocity_right * 1.2
