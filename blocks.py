from block import Block
from position import Position

class LBlock(Block):
    '''
    LBlock and the positions of its rotations
    '''
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)],
        }

        self.move(0,3) # To centre block upon initialisation

class JBlock(Block):
    '''
    JBlock and the positions of its rotations
    '''
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
            3: [Position(0,1), Position(1,1), Position(2,0), Position(2,1)],
        }

        self.move(0,3) # To centre block upon initialisation

class IBlock(Block):
    '''
    IBlock and the positions of its rotations
    '''
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)],
        }

        self.move(-1,3) # To centre block upon initialisation

class OBlock(Block):
    '''
    OBlock and the positions of its rotations. Only has 1 rotation as it is in the same position every 
    rotation
    '''
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            #1: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            #2: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            #3: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
        }

        self.move(0,4) # To centre block upon initialisation

class SBlock(Block):
    '''
    SBlock and the positions of its rotations
    '''
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2: [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],
            3: [Position(0,0), Position(1,0), Position(1,1), Position(2,1)],
        }
        
        self.move(0,3) # To centre block upon initialisation

class TBlock(Block):
    '''
    TBlock and the positions of its rotations
    '''
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,1)],
        }

        self.move(0,3) # To centre block upon initialisation

class ZBlock(Block):
    '''
    ZBlock and the positions of its rotations
    '''
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],
            1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,0)],
        }

        self.move(0,3) # To centre block upon initialisation