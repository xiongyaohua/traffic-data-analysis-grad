from multiprocessing import connection, Process

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

world.add_wall((400, 300), (600, 300))

robot = world.add_robot(500, 500)
for angle in np.linspace(0, 2 * np.pi, 6)[1:-1]:
    robot.add_laser(angle)
robot.add_laser(0.0, True)

state = {}

FPS = 60
def main():
    pygame.init()
    screen=pygame.display.set_mode((window_width, window_height))

    with connection.Listener("127.0.0.1:6006") as listener:
        with listener.accept() as conn:
            running = True
            clock = pygame.time.Clock()
            while running:
                for events in pygame.event.get():
                    if events.type == QUIT:
                        running = False

                world.process(1.0 / FPS)

                screen.fill(screen_color)
                world.draw(screen)
                pygame.display.flip()

                state["time"] = clock.get_time()
                conn.send(state)
                clock.tick(FPS) # 刷新率控制在60fps

main()
pygame.quit()
