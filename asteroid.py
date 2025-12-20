import pygame
import constants
import random
from circleshape import CircleShape
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position = self.position  + (self.velocity * dt) 

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        rotated_vector_2 = self.velocity.rotate(random_angle)
        rotated_vector_3 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = (rotated_vector_2 * 1.2)
        new_asteroid_2.velocity = (rotated_vector_3 * 1.2)
        return new_asteroid_1, new_asteroid_2