import pygame
import constants
import player
import asteroid
import asteroidfield
from logger import log_state, log_event
import sys
import shot


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
    shots = pygame.sprite.Group()
    
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield.AsteroidField.containers = (updatable,)
    asteroidfield.AsteroidField()

    player.Player.containers = (updatable, drawable)
    player_one = player.Player((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
    
    shot.Shot.containers = (updatable, drawable, shots)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")
        
        updatable.update(dt)

        for each_asteroid in asteroids:
            if each_asteroid.collides_with(player_one):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for each_asteroid in asteroids:
            for each_shot in shots:
                if each_shot.collides_with(each_asteroid):
                    log_event("asteroid_shot")
                    each_shot.kill()
                    each_asteroid.kill()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
