import pygame
from time import sleep

from menu import menu
from graph import Graph
from dfs import DFS
from bfs import BFS
from ucs import UCS
from gbfs import GBFS
from a_star import AStar

WIDTH = 800
ROWS = 20
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("search algorithms")
pygame.font.init()

RED = (0, 93, 156)
GREEN = (156, 191, 247)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

def reconstruct_path_alg(solution, grid, draw):
    solution.pop(0)
    solution.pop(-1)
    for node in solution:
        x = node.x
        y = node.y
        grid[x][y].make_path()
        sleep(0.01)
        draw()

def expanded(visited, frontier, grid, start, goal, draw):
    for node in frontier:
        x = node.x
        y = node.y

        start_x = start.row
        start_y = start.col
        goal_x = goal.row
        goal_y = goal.col

        if not (start_x == x and start_y == y) and not (goal_x == x and goal_y == y):
            grid[x][y].make_open()

    for node in visited:
        x = node.x
        y = node.y

        start_x = start.row
        start_y = start.col
        goal_x = goal.row
        goal_y = goal.col

        if not (start_x == x and start_y == y) and not (goal_x == x and goal_y == y):
            grid[x][y].make_closed()
    
    draw()

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))

def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col

def algorithms(window, width, alg = "dfs"):
    grid = make_grid(ROWS, width)

    start = None
    end = None
    run = True
    started = False
    
    draw(window, grid, ROWS, width)
    while run:
        draw(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            draw(window, grid, ROWS, width)
            if pygame.mouse.get_pressed()[0]: #Left button mouse
                pos = pygame.mouse.get_pos()
                col, row = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                
                elif not end and node != start:
                    end = node
                    end.make_end()
                
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #Right button mouse
                pos = pygame.mouse.get_pos()
                col, row = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    if start != None and end != None:
                        formated_draw = lambda: draw(window, grid, ROWS, width)
                        formated_expanded = lambda visited, frontier: expanded(visited, frontier, grid, start, end, formated_draw)
                        graph = Graph(grid, start, end)
 

                        if alg == "dfs":
                            # ======= Busca em Profundidade ======
                            DFS(graph).solve(formated_draw, reconstruct_path_alg, formated_expanded)
                        elif alg == "bfs":
                            # ========= Busca em Largura =========
                            BFS(graph).solve(formated_draw, reconstruct_path_alg, formated_expanded)
                        elif alg == "ucs":
                            # ===== Busca de Custo Uniforme  =====
                            UCS(graph).solve(formated_draw, reconstruct_path_alg, formated_expanded)
                        elif alg == "gbfs":
                            # = Busca Gulosa pela Melhor Escolha =
                            GBFS(graph).solve(formated_draw, reconstruct_path_alg, formated_expanded)
                        elif alg == "a*":
                            # ================ A* ================
                            AStar(graph).solve(formated_draw, reconstruct_path_alg, formated_expanded)

                if event.key == pygame.K_ESCAPE:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_m:
                    menu(WIN, WIDTH, algorithms)

                if event.key == pygame.K_c:
                    for i in range(ROWS):
                        for j in range(ROWS):
                            current = grid[i][j].color
                            if current == GREEN or current == RED or current == PURPLE:
                                grid[i][j].color = WHITE
    pygame.quit()