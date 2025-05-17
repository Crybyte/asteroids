import pygame

from circleshape import CircleShape

import random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        old_radius = self.radius
        old_velocity = self.velocity

        self.kill()

        if (old_radius <= ASTEROID_MIN_RADIUS):
            return

        random_angle = random.uniform(20, 50)

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        pos = self.position

        newOne = Asteroid(pos.x, pos.y, new_radius)
        newOne.velocity = old_velocity.rotate(random_angle) * 1.2

        newTwo = Asteroid(pos.x, pos.y, new_radius)
        newTwo.velocity = old_velocity.rotate(-random_angle) * 1.2

