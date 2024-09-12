from world import World

world = World()

# 添加八角形房间
angles = np.linspace(0.0, 2 * np.pi, 9)
points = [(np.cos(angle), np.sin(angle)) for angle in angles]
points = [(p[0]*400+500, p[1]*400+500) for p in points]
for p1, p2 in zip(points[0:-1], points[1:]):
    world.add_wall(p1, p2)


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