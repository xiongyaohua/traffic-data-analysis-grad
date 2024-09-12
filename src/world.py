from pygame import math
from pygame.math import Vector2
from theme import wall_color

class World:
    def __init__(self):
        self.walls = []

    def add_wall(self, start, end):
        start = Vector2(start)
        end = Vector2(end)
        self.walls.append((start, end))

    def show(self, screen):
        for wall in self.walls:
            pygame.draw.line(screen,wall_color, wall[0], wall[1], 10)
        
    def ray_trace(self, position, direction):
        pass