import pygame
from pygame.math import Vector2
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
from theme import robot_color

SPEED = 50 # pixel per second

class Robot:
    def __init__(self, x: float=0.0, y: float=0.0, size: float=10):
        self.position = Vector2(x, y)
        self.size = size

    def process(self, dt: float):
        pressed = pygame.key.get_pressed()

        v = Vector2()
        if pressed[K_UP]:
            v.y -= 1.0
        if pressed[K_DOWN]:
            v.y += 1.0
        if pressed[K_LEFT]:
            v.x -= 1.0
        if pressed[K_RIGHT]:
            v.x += 1.0

        self.position += v * SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen, robot_color, self.position, self.size)