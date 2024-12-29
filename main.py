import pygame
from constants import *
from player import *

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

    Player.containers = (updatable, drawable)

    player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") 

        for d in drawable: 
            d.draw(screen)

        for u in updatable:
            u.update(dt)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
