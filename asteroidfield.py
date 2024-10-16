import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):

    def __init__(self, screen, game_state):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game_state = game_state
        self.screen = screen
        self.spawn_timer = 0.0
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * screen.get_height()),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    screen.get_width() + ASTEROID_MAX_RADIUS, y * screen.get_height()
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * screen.get_width(), -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * screen.get_width(), screen.get_height() + ASTEROID_MAX_RADIUS
                ),
            ],
        ]

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100 + (self.game_state.level * 20))
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * self.screen.get_height()),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.screen.get_width() + ASTEROID_MAX_RADIUS, y * self.screen.get_height()
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * self.screen.get_width(), -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * self.screen.get_width(), self.screen.get_height() + ASTEROID_MAX_RADIUS
                ),
            ],
        ]
