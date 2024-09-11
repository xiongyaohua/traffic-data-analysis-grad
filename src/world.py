import pygame
import numpy as np
from pygame.locals import QUIT

E = 0.00001

class World:
    def __init__(self):
        self.walls = []

    def add_wall(self, start, end):
        self.walls.append((start, end))

    def show(self, screen):
        for wall in self.walls:
            pygame.draw.line(screen,line_color, wall[0], wall[1], 10)
        
def _line_and_line(line1, line2):
    A = np.array([
        line1,
        line2
    ], dtype=float)
    b = np.array([-1, -1], dtype=float)
    # TODO:处理平行的情况
    p = np.linalg.solve(A, b)
    return p

def _distance(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    d = p1 - p2
    return np.sqrt(np.dot(d, d))   

def _point_on_segment(p, p1, p2):
    p_p1 = _distance(p, p1)
    p_p2 = _distance(p, p2)
    p1_p2 = _distance(p1, p2)

    return np.abs(p_p1 + p_p2 - p1_p2) < E

def _ray_trace(position, direction, wall):
    # 光线->直线
    tmp = (position[0] * direction[1] - direction[0] * position[1])
    a1 = direction[0] / tmp
    b1 = -direction[1] / tmp
    # 墙->直线
    # TODO
    a2 = None
    b2 = None

    line1 = (a1, b1)
    line2 = (a2, b2)
    intersection = _line_and_line(line1, line2)
    if intersection is None:
        return None

    if not _point_on_segment(intersection, p1, p2):
        return None

    direction_to_intersection = (
        intersection[0] - position[0],
        intersection[1] - position[1],
        )
    
    if np.dot(direction, direction_to_intersection) > 0.0:
        return intersection
    else:
         None

def ray_trace(position, direction, walls):
    intersections = [_ray_trace(position, direction, wall) for wall in walls]
    intersections.remove(None)
    if not intersections:
        return None
    
    intersections.sort(
        key=lambda intersection: _distance(intersection, position)
    )

    return intersections[0]

world = World()

# 添加八角形房间
angles = np.linspace(0.0, 2 * np.pi, 9)
points = [(np.cos(angle), np.sin(angle)) for angle in angles]
points = [(p[0]*400+500, p[1]*400+500) for p in points]
for p1, p2 in zip(points[0:-1], points[1:]):
    world.add_wall(p1, p2)

width = 1000
height = 1000
screen_color = (220, 220, 220)
line_color = (200, 100, 100)

def main():
    pygame.init()
    screen=pygame.display.set_mode((width,height))

    running = True
    while running:
        screen.fill(screen_color)
        world.show(screen)
        pygame.display.flip()
        for events in pygame.event.get():
            if events.type == QUIT:
                running = False

main()
pygame.quit()
