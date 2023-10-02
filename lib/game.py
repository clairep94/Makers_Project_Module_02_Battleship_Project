from lib.ship import Ship
from lib.player import Player

class Game:
    def __init__(self, rows=10, cols=10, ship_sizes = [2, 3, 3, 4, 5]):
        '''
        Initialises a game with the specified dimensions, 2 players with empty boards, and two identical sets of ships sizes
        '''
        self.rows = rows #10 is default
        self.cols = cols #10 is default
        self.unplaced_ships_player_one = ship_sizes #[2, 3, 3, 4, 5] is default
        self.unplaced_ships_player_two = ship_sizes #[2, 3, 3, 4, 5] is default

        player_1 = Player(rows=rows, columns=cols)
        player_2 = Player(rows=rows, columns=cols)
        self.players = [player_1, player_2]
        
        self.turn = 0

    def place_ship(self, player_num:int, length:int, orientation:str, row:int, col:int) -> None:
        '''
        Params: 
            player - int [1,2] representing player 1 or player 2 that is placing the ship
            length - int representing length of Ship object
            orientation - str, either 'horizontal' or 'vertical',
            row - int representing row on the board
            col - int representing col

        Returns: none | Exception if ship is overlapping another ship or ship is out of bounds.
        Side Effects: player adds ship to their board and their player.ships list. self.unplaced_ships removes
        the corresponding ship size from the corresponding player.
        '''
        player_num -= 1 #convert from 1-start index to 0-start index
        player = self.players[player_num]

        placement_message = player.place_ship(ship=Ship(length=length), orientation=orientation, row=row, col=col)
        if placement_message != None:
            return placement_message
        else:
            if player_num == 0:
                self.unplaced_ships_player_one.remove(length)
            # else:
            #     self.unplaced_ships_player_two.remove(length)

    # def ship_at(self, row, col):
    #     '''
    #     Returns True if ship is at row/col
    #     '''
    #     for ship_placement in self.ships_placed:
    #         if ship_placement.covers(row, col):
    #             return True
    #     return False
