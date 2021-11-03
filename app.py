import pygame

from menu import menu
from algorithms import algorithms

class App:
    def __init__(self, width):
        self.width = width
        self.screen = pygame.display.set_mode((width, width))

    def run(self):
        menu(self.screen, self.width, algorithms)