import pygame
import constants
import player
import asteroid
import asteroidfield
from logger import log_state

pygame.init()
clock = pygame.time.Clock()
dt = 0

def main():
    print(f"Starting Asteroids with pygame version: {str(pygame.version.vernum)}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield.AsteroidField.containers = (updatable,)
    asteroidfield.AsteroidField()

    player.Player.containers = (updatable, drawable)
    player_one = player.Player((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")
        
        updatable.update(dt)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
