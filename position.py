class Position:
    '''
    Position class of blocks that child classes can inherit
    '''
    def __init__(self, row, column):
        self.row = row
        self.column = column