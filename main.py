import pygame
import sys
from grid import Grid
from blocks import *
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

# Create the display screen
screen = pygame.display.set_mode((300, 600)) # Set width and height of display surface
pygame.display.set_caption("Python Tetris") # Title

clock = pygame.time.Clock() # To control frame rate and how fast game runs

#game_grid = Grid()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 20)

#block = TBlock()
#block = LBlock()
#block = OBlock()
#block = SBlock()
#block = JBlock()
#block = IBlock()
#block = ZBlock()

#game_grid.print_grid()

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
        if event.type == pygame.KEYDOWN :
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Drawing the objects
    screen.fill(dark_blue)
    game.draw(screen)
    #game_grid.draw(screen)
    #block.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # 60 frames per second