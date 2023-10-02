from lib.player import Player
from lib.ship import Ship
from unittest import mock
import pytest


'''Test initialising a default board'''
def test_player_init_with_default_board():
    player_1 = Player()
    assert player_1.ships == []
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''Test placing a horizontal ship on a default board'''
def test_place_ship():
    player_1 = Player()
    ship = Ship(4)
    player_1.place_ship(ship=ship, orientation="horizontal", row=3, col=4)
    assert ship.orientation == "horizontal"
    assert ship.units == [
        {'hit': False, 'coordinates': (2, 3)},
        {'hit': False, 'coordinates': (2, 4)},
        {'hit': False, 'coordinates': (2, 5)},
        {'hit': False, 'coordinates': (2, 6)},
    ]
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

'''Test placing a vertical ship on a default board'''
def test_place_ship():
    player_1 = Player()
    ship = Ship(4)
    player_1.place_ship(ship=ship, orientation="vertical", row=3, col=4)
    assert ship.orientation == "vertical"
    assert ship.units == [
        {'hit': False, 'coordinates': (2, 3)},
        {'hit': False, 'coordinates': (3, 3)},
        {'hit': False, 'coordinates': (4, 3)},
        {'hit': False, 'coordinates': (5, 3)},
    ]
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


'''
Catch error for placing a ship out of bounds
'''
def test_error_place_ship_out_of_bounds():
    player_1 = Player()
    ship = Ship(4)
    with pytest.raises(Exception) as e:
        player_1.place_ship(ship=ship, orientation="horizontal", row=9, col=9)
    assert str(e.value) == "Ship placement out of bounds."