from grid import Grid
from blocks import *
import random
import pygame

class Game:
    '''
    Game Logic
    '''
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1) # -1 to indicate it should loop indefinitely

    def update_score(self, lines_cleared, move_down_points):
        '''
        This method calculates the score. Takes as arguments number of lines cleared and the total move 
        down points. Returns the score.

        If 1 line is cleared, add 100 points, if 2 lines are cleared at once, add 300 points, if 3 lines
        are cleared at once, add 500 points.
        '''
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def get_random_block(self):
        '''
        Get a random block every time, making sure every block is encountered once before repeating from 
        list.
        '''
        if len(self.blocks) == 0: # Restart when every block has appeared
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        
        block = random.choice(self.blocks)
        self.blocks.remove(block) # Remove from list to get other blocks
        return block
    
    def move_left(self):
        '''
        Move left
        '''
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        '''
        Move right
        '''
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits == False:
            self.current_block.move(0, -1)

    def move_down(self):
        ''''
        Move down
        '''
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        '''
        Lock position of block when it reaches the bottom
        '''
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play() # Play sound when a row or rows is/are cleared
            self.update_score(rows_cleared, 0) # Update score
        if self.block_fits() == False: # Check if any more blocks can fit
            self.game_over = True

    def reset(self):
        '''
        Reset game
        '''
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        '''
        Check if a block is able to fit. Returns a Boolean value
        '''
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False # Cell positions are not empty
        return True # Able to fit

    def rotate(self):
        '''
        Rotate block accorinding to their positions
        '''
        self.current_block.rotate() # Rotate
        if self.block_inside() == False: # If block goes outside the boudaries:
            self.current_block.undo_rotation() # Undo move
        else:
            self.rotate_sound.play() # Play the rotation sound
    
    def block_inside(self):
        '''
        Check if a block is inside the boundaries. Returns a Boolean value
        '''
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        '''
        Draw grid
        '''
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)