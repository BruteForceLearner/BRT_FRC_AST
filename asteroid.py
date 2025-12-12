import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            (self.radius),
            (LINE_WIDTH),
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_velocity_one = self.velocity.rotate(-angle)
        new_velocity_two = self.velocity.rotate(+angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_one.velocity = new_velocity_one * 1.2
        new_ast_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_two.velocity = new_velocity_two * 1.2
