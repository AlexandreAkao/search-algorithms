import re

class Maze:
    size = []
    start = []
    goal = []

    def __init__(self):
        self.create_maze([8, 8], [2, 1], [2, 6])

    def create_maze(self, size, start, goal):
        self.size = size
        self.start = start
        self.goal = goal

    def can_pass(self, row, column, direction, grid):
        if direction == "east":
            if column == (self.size[1] - 1):
                return False
            return grid[row + 1][column].make_barrier()
        elif direction == "south":
            if row == (self.size[0] - 1):
                return False
            return grid[row][column + 1].make_barrier()
        elif direction == "west":
            if column == 0:
                return False
            return grid[row - 1][column].make_barrier()
        elif direction == "north":
            if row == 0:
                return False
            return grid[row][column - 1].make_barrier()
