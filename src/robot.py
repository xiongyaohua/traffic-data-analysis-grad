import pygame
from pygame.math import Vector2
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
from theme import robot_color, laser_color
from geometry import intersect_ray_with_segments

SPEED = 50.0 # pixel per second
SCAN_SPEED = 1.0 # rad per second
class Laser:
    def __init__(self, direction: Vector2=Vector2(0, -1), rotating=False):
        self.direction = direction
        self.rotating = rotating
        hit = None

    def process(self, dt: float, position, walls):
        if self.rotating:
            self.direction.rotate_rad_ip(SCAN_SPEED * dt)

        ray = (position, self.direction)
        self.hit = intersect_ray_with_segments(ray, walls)

    def draw(self, screen, position):
        if self.hit:
            pygame.draw.line(screen, laser_color, position, self.hit)
            pygame.draw.circle(screen, laser_color, self.hit, 5)
        else:
            pygame.draw.line(
                screen, laser_color, position,
                position + self.direction * 1000
            )

class Robot:
    def __init__(self, x: float=0.0, y: float=0.0, size: float=10):
        self.position = Vector2(x, y)
        self.size = size
        self.lasers: list[Laser] = []

    def add_laser(self, angle: float=0.0, rotating=False):
        direction = Vector2(0, -1).rotate_rad(angle)
        laser = Laser(direction, rotating)
        self.lasers.append(laser)

    def process(self, dt: float, world):
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

        for laser in self.lasers:
            laser.process(dt, self.position, world.walls)

    def draw(self, screen):
        for laser in self.lasers:
            laser.draw(screen, self.position)
        
        pygame.draw.circle(screen, robot_color, self.position, self.size)
