import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updateable, drawable, shots)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    field = AsteroidField()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # start of game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for object in updateable:
            object.update(dt)
        for object in asteroids:
            if object.check_collision(player) is True:
                print("Game Over!")
                sys.exit()
        for object in asteroids:
            for bullet in shots:
                if object.check_collision(bullet) is True:
                    object.split()
                    bullet.kill()
        for object in drawable:
            object.draw(screen)
        # flip() the display to put your work on screen (everything that needs
        # rendered goes before this)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
