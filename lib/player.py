from lib.ship import Ship

class Player:
    def __init__(self, rows:int=10, columns:int=10) -> None:
        '''
        Stores player data including a list of Ship objects, as well as the player's own board. The status of each space on the player's own board
        is stored as a code in self.board_statuses. 
        self.board of each player gets interpretted in user_interface so that at each turn, each player
        can see their own board, as well as a hidden version of their opponent's board.
        '''
        self.rows = rows
        self.columns = columns
        self.ships = [] #list of ship objects
        self.board = self.create_board(rows=rows, columns=columns) #status of each space on the player's own board
        # -- empty, ship, miss, hit, full_ship_hit
        self.board_statuses = {
            0: "empty", # "*"
            1: "ship", # "S" or "*"
            2: "miss", # "/"
            3: "hit", # "x"
            4: "full_ship_hit" # "X"
        }

    def create_board(self, rows, columns) -> list:
        '''
        Params: rows & columns
        Returns: none
        Effects: creates a fresh board with dimenions specified. Default is 10 x 10 spaces.
        '''
        board = []
        for i in range(rows):
            row = [0 for i in range(columns)] #each row has {columns} 0's
            board.append(row)
        return board
    
    def place_ship(self, ship:Ship, orientation:str, row:int, col:int) -> None:
        '''
        Params: Ship object, orientation, row & column
        Returns: none
        Side effects: adds new ship object to self.ships, updates the board? 
        CHECK IF SHIP IS IN BOUNDS -- check if the unit coordinate of the last unit is out of bounds (ie if len(row) or len(board) < last coordinate)
        '''
        # call .place_ship() method from Ship class.
        # method changes coordinates to 0-based indexing
        # ship now stores hit status and coordinates for each unit
        ship.place_ship(orientation=orientation, row=row, col=col)

        # check the last unit of ship.units to check that the ship placement is not out of bounds.
        last_ship_unit_coordinates = ship.units[-1]["coordinates"]
        if last_ship_unit_coordinates[0] > self.rows or last_ship_unit_coordinates[1] > self.columns:
            raise Exception("Ship placement out of bounds.")

        # iterate through each unit of ship.units, and change status code of the matching board space
        # to 1.
        for unit in ship.units:
            r = unit["coordinates"][0]
            c = unit["coordinates"][1]
            self.board[r][c] = 1


    def update_board():
        '''
        Params: none
        Returns: self.board
        Side effects: gets all data from self.
        '''
        pass


    def check_for_hit(row:int, col:int) -> None:
        '''
        Params: row and column of space to check.

        Returns & Side Effects:
        Check if board space status for the coordinates provided have a code 0 or 1.
        If code 0 ("empty") --> change space status to 2 ("miss") --> Return "miss"
        If code 1 ("ship") --> change space status to 3 ("hit"). --> Return "hit"
            Then check if the ship hit was sank. If so, change all spaces for that ship to code 4. --> Return "sank"
        '''
        pass