import re

class Maze:
    grid = []
    size = []
    start = []
    goal = []

    def __init__(self, grid, start, goal):
        self.create_maze(grid, start, goal)

    def create_maze(self, grid, start, goal):
        size = len(grid)

        self.grid = grid
        self.size = [size, size]
        self.start = None if start == None else [start.row, start.col] 
        self.goal = None if start == None else [goal.row, goal.col]

    def can_pass(self, row, column, direction):
        if direction == "east":
            if row >= (self.size[1] - 1):
                return False
            return not self.grid[row + 1][column].is_barrier()
        elif direction == "south":
            if column >= (self.size[0] - 1):
                return False
            return not self.grid[row][column + 1].is_barrier()
        elif direction == "west":
            if row <= 0:
                return False
            return not self.grid[row - 1][column].is_barrier()
        elif direction == "north":
            if column <= 0:
                return False
            return not self.grid[row][column - 1].is_barrier()
