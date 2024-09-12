import pygame
from pygame.math import Vector2
from theme import wall_color
from robot import Robot
from geometry import Segment

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