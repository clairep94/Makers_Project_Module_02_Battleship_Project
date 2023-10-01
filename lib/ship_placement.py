class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        '''
        Stores the length and orientation of the ship, as well as the row/col of the first unit of the ship.'''
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col

    def covers(self, row, col):
        '''
        Checks if there is a ship in a certain row/column
        '''
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
