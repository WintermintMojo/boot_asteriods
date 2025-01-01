import pygame
from circleshape import CircleShape
from constants import *

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH:
            self.kill()
        if self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.kill()