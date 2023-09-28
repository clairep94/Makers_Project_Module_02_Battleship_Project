class UserInterface:
    def __init__(self, io, game):
        self.io = io 
        self.game = game 

    def run(self): 
        #MAIN FUNCTION HERE

        #1) GAME INTRO -- change into function
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message()))
        
        #2) PLACING SHIPS TO BOARD:
        # Alternate player's abilities to place ships on the board. 
        
        # placing_ships_stage = True
        # player_to_go = "1" #start with player one
        # turn = 1
        while len(self.game.unplaced_ships()) > 0: #while there are still ships left to place:

            # #alternate between players one and two
            # if turn % 2 == 0:
            #     player_to_go = "2"
            # else:
            #     player_to_go = "1" 

        #INDENT THE BELOW WHEN YOU ADD MORE PLAYERS:

            #Show board before ship placement.
            self._show("This is your current board:")
            self._show(self._format_board())

            # Prompt to place one ship.
            # TEST!!! If you can overlap ships.
            # TEST!!! If you can place ships beyond the game borders.
            self._prompt_for_ship_placement()

            #Show resulting board
            self._show("This is your board now:")
            self._show(self._format_board())


        #3) START ATTACKING;
        # create a new _format_board() so that it prints a clear board initially (+'s)
        # each time the player hits an empty square, change the square to (-)
        # each time the player hits a ship, change the square to (X)
        # Loop until all units are NOT + OR all opponent ships are hit.

        # Create opponent ship list. - initially these can be me vs. me
        # Create opponent ship board. - initially these can be my board reset.




######-------------------FUNCTIONS CALLED-------------------#####

    #INPUT/PRINT FUNCTIONS:
    def _show(self, message): #print to terminal, returns nothing
        self.io.write(message + "\n")
    def _prompt(self, message): #equivalant to input(message + "\n")
        self.io.write(message + "\n")
        return self.io.readline().strip()


###---------------------------------------##


    def _ships_unplaced_message(self): 
        '''
        Prints remaining ships represented by their length in a string.
        2, 3, 4, 5 to start.
        '''
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships()]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self): 
        '''
        Params: none, Returns: none.
        
        Takes Inputs for:
        1) ship size
        2) orientation of placement
        3) row and column of placement

        Effects: places ship
        '''
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")
        self._show("OK.")
        self.game.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )


    def _format_board(self): #CHANGE THIS TO TAKE IN PLAYER 1 vs. 2
        '''
        For unfilled 
        '''
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append("+")
            rows.append("".join(row_cells))
        return "\n".join(rows)
