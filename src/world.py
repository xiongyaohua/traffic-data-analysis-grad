import pygame
from pygame.math import Vector2
from theme import wall_color
from robot import Robot
from geometry import Segment, intersect_ray_with_segments
import numpy as np

class World:
    def __init__(self):
        self.walls: list[Segment] = []
        self.robots: list[Robot] = []

    def add_wall(self, start: Vector2, end: Vector2):
        start = Vector2(start)
        end = Vector2(end)
        self.walls.append((start, end))

    def add_robot(self, x: float=0.0, y: float=0.0, size: float=10):
        robot = Robot(x, y, size)
        self.robots.append(robot)
        return robot

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.line(screen, wall_color, wall[0], wall[1], 10)
        
        for robot in self.robots:
            robot.draw(screen)
        
    def process(self, dt):
        for robot in self.robots:
            robot.process(dt, self)

    def sense(self):
        if self.robots:
            return {
                "lasers": self.robots[0].sense()
            }
        else:
            return {}

    def ray_trace(self, pos, alpha):
        direction = Vector2(0, -1)
        direction.rotate_ip(alpha)
        ray = (pos, direction)
        hit = intersect_ray_with_segments(ray, self.walls)
        if hit:
            return hit.distance_to(pos)
        else:
            return np.inf

import unittest

class TestWorldRayTrace(unittest.TestCase):
    def test_ray_trace(self):
        world = World()
        world.add_wall((400, 300), (600, 300))
        pos = Vector2(500, 500)
        
        hit = world.ray_trace(pos, 0)
        self.assertEqual(hit, 200)
        
        pos = Vector2(500, 350)
        hit = world.ray_trace(pos, 45)
        self.assertEqual(hit, 70.7106)

if __name__ == "__main__":
    unittest.main()