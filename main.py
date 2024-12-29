import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)


    asteroidField = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") 

        for d in drawable: 
            d.draw(screen)

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            is_colliding = player.collision_detection(a)
            if is_colliding:
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                is_colliding = shot.collision_detection(a)
                if is_colliding:
                    a.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
