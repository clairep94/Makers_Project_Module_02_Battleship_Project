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
def test_place_ship_horizontal():
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
def test_place_ship_vertical():
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


'''
Checking for hit on an empty space
'''
def test_check_for_hit_empty_space():
    player_1 = Player()
    ship = Ship(4)
    player_1.place_ship(ship=ship, orientation="vertical", row=3, col=4)
    assert player_1.check_for_hit(row=2, col=1) == "miss"
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
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
Checking for hit on a ship space
'''
def test_check_for_hit_ship_space():
    player_1 = Player()
    ship = Ship(4)
    player_1.place_ship(ship=ship, orientation="vertical", row=3, col=4)
    assert player_1.check_for_hit(row=4, col=4) == "hit"
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

'''
Checking for sank ship
'''
def test_check_for_sank_ship():
    player_1 = Player()
    ship = Ship(3)
    player_1.place_ship(ship=ship, orientation="vertical", row=3, col=4)
    assert player_1.check_for_hit(row=4, col=4) == "hit"
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert player_1.check_for_hit(row=3, col=4) == "hit"
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert player_1.check_for_hit(row=5, col=4) == "sank"
    assert player_1.board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert player_1.ships[0].units == [
        {'hit': True, 'coordinates': (2, 3)},
        {'hit': True, 'coordinates': (3, 3)},
        {'hit': True, 'coordinates': (4, 3)}
    ]