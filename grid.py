import pygame
from colours import Colours

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 # Size of each grid's pixel, 30 x 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # Create a list of lists using list comprehension
        self.colours = Colours.get_cell_colours()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print() # Iterate over every line with each each row printed on a new line
 
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size-1, self.cell_size-1) # x, y, width and height of each rectangle pixel. Make it 29 x 29 pixels to create a 1 pixel margin
                pygame.draw.rect(screen, self.colours[cell_value], cell_rect)