import pygame
import sys
from grid import Grid
from blocks import *
from game import Game
from colours import Colours

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colours.white)
next_surface = title_font.render("Next", True, Colours.white)
game_over_surface = title_font.render("GAME OVER", True, Colours.white)

score_rect = pygame.Rect(320, 55, 170, 60) # x and y coordinates, width and height of rectangle
next_rect = pygame.Rect(320, 215, 170, 180)


# Create the display screen
screen = pygame.display.set_mode((500, 620)) # Set width and height of display surface
pygame.display.set_caption("Python Tetris") # Title

clock = pygame.time.Clock() # To control frame rate and how fast game runs

#game_grid = Grid()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

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
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Drawing the objects
    score_value_surface = title_font.render(str(game.score), True, Colours.white)

    screen.fill(Colours.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colours.light_blue, score_rect, 0, 10) # Rounded rectangle to display score
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colours.light_blue, next_rect, 0, 10) # Rounded rectangle to display next block
    game.draw(screen)
    #game_grid.draw(screen)
    #block.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # 60 frames per second