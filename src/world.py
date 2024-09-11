import pygame
from pygame.locals import QUIT

class World:
    def __init__(self):
        self.walls = []

    def add_wall(self, start, end):
        self.walls.append((start, end))

    def show(self, screen):
        for wall in self.walls:
            pygame.draw.line(screen,line_color, wall[0], wall[1], 10)
        

world = World()
world.add_wall((1, 1), (500,500))

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
