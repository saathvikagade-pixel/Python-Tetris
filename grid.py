class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 # Size of each grid's pixel, 30 x 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # Create a list of lists using list comprehension
        self.colours = self.get_cell_colours()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print() # Iterate over every line with each each row printed on a new line

    def get_cell_colours(self):

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]