import sys
import pygame
from constants import *
from gamestate import GameState
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0 #delta time

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    GameState.containers = (updatables, drawables)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    # initialization
    game_state = GameState()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField(screen, game_state)

    while True:
        # allow game to close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update screen
        screen.fill('black')

        # update and draw
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                sys.exit()
            for shot in shots:
                if asteroid.is_colliding(shot):
                    game_state.scored(asteroid)
                    asteroid.split()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)

        # refresh
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
