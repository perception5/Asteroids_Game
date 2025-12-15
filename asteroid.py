import pygame
import constants
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position = self.position  + (self.velocity * dt) 
