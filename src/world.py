class World:
    def __init__(self):
        self.walls = []

    def add_wall(self, start, end):
        self.walls.append((start, end))

    def show(self):
        print(self.walls)

world = World()
world.add_wall((1, 1), (2,2))
world.show()
