class Ship:
    def __init__(self, length:int) -> None:
        '''
        Stores the length, orientation, and status and coordinates of the individual units of the ship.
        '''
        self.length = length
        self.sank = False

        self.orientation = None
        self.units = []

    def place_ship(self, orientation, row, col) -> None:
        '''
        Creates a nested dictionary storing all units of the ship, their individual hit status,
        and their individual coordinate (row, col). Note that coordinates are stored in 0-based indexing.
        Updates self.orientation and self.units
        Returns: none
        '''
        #convert to 0-based indexing for checking against our board array
        row -= 1
        col -= 1
        self.units = []

        #Vertical ship:
        self.orientation = orientation
        if orientation == "vertical":
            units = [{"hit": False, "coordinates": ((row + i), col)} for i in range(self.length)]

        #Horizontal ship:
        elif orientation == "horizontal":
            for i in range(self.length):
                units = [{"hit": False, "coordinates": (row, (col + i))} for i in range(self.length)]

        #Update ship.units to units. Units coordinates are stored in 0-based indexing.
        self.units = units


    def ship_at(self, row:int, col:int) -> bool:
        '''
        Checks through the unit coordinates to see if any are a match for the coordinates inputted
        '''
        #convert to 0-based indexing for checking against our board array
        row -= 1
        col -= 1

        return any(unit["coordinates"] == (row, col) for unit in self.units)
    
    def check_if_sank(self) -> bool:
        '''
        Params: None
        Returns: True if all unit['hit'] in ship.units are True, meaning that all units in the ship have been hit
        and ship has sank.

        '''
        return all(unit['hit'] for unit in self.units)