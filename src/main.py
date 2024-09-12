import numpy as np
import pygame
from pygame.locals import QUIT
from world import World
from robot import Robot
from theme import window_width, window_height, screen_color

world = World()

# 添加八角形房间
angles = np.linspace(0.0, 2 * np.pi, 9)
points = [(np.cos(angle), np.sin(angle)) for angle in angles]
points = [(p[0]*400+500, p[1]*400+500) for p in points]
for p1, p2 in zip(points[0:-1], points[1:]):
    world.add_wall(p1, p2)

robot = Robot(500, 500)

FPS = 60
def main():
    pygame.init()
    screen=pygame.display.set_mode((window_width, window_height))

    running = True
    clock = pygame.time.Clock()
    while running:
        for events in pygame.event.get():
            if events.type == QUIT:
                running = False

        robot.process(1.0 / FPS)

        screen.fill(screen_color)
        world.draw(screen)
        robot.draw(screen)
        pygame.display.flip()

        clock.tick(FPS) # 刷新率控制在60fps

main()
pygame.quit()
