from lib.ship import Ship

"""
Initialises with a given length
"""

def test_initialises_with_a_given_length():
    ship = Ship(length=5)
    assert ship.length == 5
