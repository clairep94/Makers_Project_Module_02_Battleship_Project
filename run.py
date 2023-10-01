import sys
from lib.game import Game
from lib.user_interface import UserInterface

#START HERE.

class TerminalIO:
    def readline(self): #captures user inputs
        return sys.stdin.readline()

    def write(self, message): #prints to terminal
        sys.stdout.write(message)


io = TerminalIO() #creates an instance of terminalIO
game = Game() #creates an instance of Game
user_interface = UserInterface(io, game) #creates an instance of UI using the io and game
user_interface.run() #see UserInterface.run() for gameplay.