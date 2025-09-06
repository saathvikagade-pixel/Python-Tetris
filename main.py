import pygame
import sys
from grid import Grid

pygame.init()
dark_blue = (44, 44, 127)

# Create the display screen
screen = pygame.display.set_mode((300, 600)) # Set width and height of display surface
pygame.display.set_caption("Python Tetris") # Title

clock = pygame.time.Clock() # To control frame rate and how fast game runs

game_grid = Grid()
game_grid.print_grid()

"""
Game Loop Code

The game loop consists of three main points to run the game smoothly:
 - Event Handling
 - Updating Positions
 - Drawing Objects
"""

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # Exit game if user quits

    # Drawing the objects
    screen.fill(dark_blue)
    
    pygame.display.update()
    clock.tick(60) # 60 frames per second