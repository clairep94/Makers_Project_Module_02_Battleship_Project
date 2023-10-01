from lib.ship import Ship


'''
Initialising a ship of a given length
'''
def test_initialises_with_a_given_length():
    ship = Ship(length=5)
    assert ship.length == 5


'''
Placing a vertical ship
'''
def test_place_ship_vertical():
    ship = Ship(5)
    ship.place_ship("vertical", 1, 2)
    assert ship.orientation == "vertical"
    assert ship.units == [
        {'hit': False, 'coordinates': (0, 1)},
        {'hit': False, 'coordinates': (1, 1)},
        {'hit': False, 'coordinates': (2, 1)},
        {'hit': False, 'coordinates': (3, 1)},
        {'hit': False, 'coordinates': (4, 1)}
        ]


'''
Placing a horizontal ship
'''
def test_place_ship_horizontal():
    ship = Ship(4)
    ship.place_ship("horizontal", 3, 4)
    assert ship.orientation == "horizontal"
    assert ship.units == [
        {'hit': False, 'coordinates': (2, 3)},
        {'hit': False, 'coordinates': (2, 4)},
        {'hit': False, 'coordinates': (2, 5)},
        {'hit': False, 'coordinates': (2, 6)},
    ]

'''
Checking if ship is a certain coordinate
'''
def test_ship_at():
    ship = Ship(4)
    ship = Ship(4)
    ship.place_ship("horizontal", 3, 4)
    assert ship.ship_at(3, 6) == True
    assert ship.ship_at(10, 10) == False