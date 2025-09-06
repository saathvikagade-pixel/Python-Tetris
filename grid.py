import pygame
from colours import Colours

class Grid:
    '''
    The grid of the game
    '''
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 # Size of each grid's pixel, 30 x 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # Create a list of lists using list comprehension
        self.colours = Colours.get_cell_colours()

    def print_grid(self):
        '''
        Print the grid of the game
        '''
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print() # Iterate over every line with each each row printed on a new line

    def is_inside(self, row, column):
        '''
        Check of blocks are within the boundaries of the grid. Takes as arguments row number and column
        number, returns a Boolean value
        '''
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):
        '''
        Check if a cell/cells are empty for block tiles to occupy. Takes as arguments row and column number
        and returns a Boolean value
        '''
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        '''
        Check if a row/rows are full. Takes a row number as argument, returns a Boolean value
        '''
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        '''
        Clear a row. Takes a row number as argument, returns cell value(s) as 0
        '''
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        '''
        If a row below is full, moves all above rows down. Takes as arguments row number and number of rows,
        returns a grid with row(s) moved down
        '''
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        '''
        Clears full row(s). Return number of completed row(s)
        '''
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        '''
        When a game is reset, empty the grid
        '''
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
 
    def draw(self, screen):
        '''
        Draw the grid
        '''
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11, self.cell_size-1, self.cell_size-1) # x, y, width and height of each rectangle pixel. Make it 29 x 29 pixels to create a 1 pixel margin
                pygame.draw.rect(screen, self.colours[cell_value], cell_rect)