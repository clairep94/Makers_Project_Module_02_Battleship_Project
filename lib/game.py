from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = [] #ShipPlacement objects
        self.rows = rows #10
        self.cols = cols #10

    def unplaced_ships(self):
        #Returns list of Ship objects
        return [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]

    def place_ship(self, length, orientation, row, col):
        #Creates a ShipPlacement objects and add to self.placed_ships
        #-> I don't really understand how the ShipPlacement class works.
        #Should also remove ships available

        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        self.ships_placed.append(ship_placement)

    def ship_at(self, row, col):
        '''
        Returns True if ship is at row/col
        
        '''
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
