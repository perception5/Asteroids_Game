import pygame
import constants
import player
from logger import log_state

pygame.init()
clock = pygame.time.Clock()
dt = 0

def main():
    print(f"Starting Asteroids with pygame version: {str(pygame.version.vernum)}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player_one = player.Player((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
        screen.fill("black")
        player_one.update(dt)
        player_one.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
