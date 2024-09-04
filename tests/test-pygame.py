import sys, pygame
from pygame.locals import*

width = 1000
height = 500
screen_color = (49, 150, 100)
line_color = (255, 0, 0)

def main():
    pygame.init()
    screen=pygame.display.set_mode((width,height))

    running = True
    while running:
        screen.fill(screen_color)
        pygame.draw.line(screen,line_color, (60, 80), (830, 100), 3)
        pygame.display.flip()
        for events in pygame.event.get():
            if events.type == QUIT:
                running = False
main()
pygame.quit()