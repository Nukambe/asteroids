import pygame
import pygame.freetype
from constants import *

class GameState(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self.level = 1
        self.font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
        self.font_surface = self.font.render(f"[Level: 1] Score: 0", False, "white", None)

    def update(self, dt):
        self.font_surface = self.font.render(f"[Level: {self.level}] Score: {self.score}", False, "white", None)

    def draw(self, screen):
        screen.blit(self.font_surface, (screen.get_width() * 0.05, screen.get_height() * 0.90))

    def scored(self, asteroid):
        if asteroid.radius == ASTEROID_MIN_RADIUS:
            self.score += 3
        elif asteroid.radius == ASTEROID_MAX_RADIUS:
            self.score += 1
        else:
            self.score += 2

        self.level = max(1, int(self.score / 10))
