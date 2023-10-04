from lib.ship import Ship
from lib.player import Player

class Game:
    def __init__(self, rows=10, cols=10):
        '''
        Initialises a game with the specified dimensions, 2 players with empty boards, and two identical sets of ships sizes
        '''
        self.rows = rows #10 is default
        self.cols = cols #10 is default
        self.player_1 = Player(rows=rows, columns=cols)
        self.player_2 = Player(rows=rows, columns=cols)
        
        self.turn = 0

    def switch_turn(self):
        self.turn += 1

    def check_game_over(self) -> bool:
        player_1_ships = self.player_1.ships
        player_2_ships = self.player_2.ships
        player_1_ship_statuses = []
        
        return self.player_1.ships

    def 

    # def place_ship(self, player_num: int, length: int, orientation: str, row: int, col: int) -> None:
    #     '''
    #     Params: 
    #         player - int [1,2] representing player 1 or player 2 that is placing the ship
    #         length - int representing length of Ship object
    #         orientation - str, either 'horizontal' or 'vertical',
    #         row - int representing row on the board
    #         col - int representing col

    #     Returns: none | Exception if ship is overlapping another ship or ship is out of bounds.
    #     Side Effects: player adds ship to their board and their player.ships list. self.unplaced_ships removes
    #     the corresponding ship size from the corresponding player.
    #     '''
    #     if player_num == 1:
    #         placement_message = self.player_1.place_ship(length=length, orientation=orientation, row=row, col=col)
    #         if placement_message is not None:
    #             return placement_message
    #     elif player_num == 2:
    #         placement_message = self.player_2.place_ship(length=length, orientation=orientation, row=row, col=col)
    #         if placement_message is not None:
    #             return placement_message

    # def ship_at(self, row, col):
    #     '''
    #     Returns True if ship is at row/col
    #     '''
    #     for ship_placement in self.ships_placed:
    #         if ship_placement.covers(row, col):
    #             return True
    #     return False
