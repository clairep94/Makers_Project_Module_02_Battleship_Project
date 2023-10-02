from lib.game import Game
import pytest

"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game = Game()
    assert game.unplaced_ships_player_one == [2, 3, 3, 4, 5]

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    game = Game()
    assert game.players[0].board == [
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
    assert game.players[1].board == [
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

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    game = Game()
    assert game.place_ship(player_num=1, length=2, orientation="vertical", row=3, col=2) == None
    assert game.players[0].board == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert game.players[1].board == [
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
    assert len(game.players[0].ships) == 1
    assert game.unplaced_ships_player_one == [3, 3, 4, 5]
    # assert game.unplaced_ships_player_two == [2, 3, 3, 4, 5]


# '''
# When we place a ship,
# We are constrained to the board
# '''
# def test_error_when_we_place_a_ship_outside_of_board():
#     game = Game()
#     with pytest.raises(Exception) as e:
#         game.place_ship(player_num=1, length=5, orientation="vertical", row=3, col=2) == None
        
#     # game.place_ship(length=5, orientation="vertical", row=7, col=2) --> throw error
#     pass


# '''
# When we place a ship,
# We cannot overlap with another ship
# '''
# def test_error_ships_cannot_overlap():
#     game = Game()
#     game.place_ship(length=2, orientation="vertical", row=3, col=2)
#     # game.place_ship(length=4, orientation="vertical", row=3, col=2) --> throw error
#     pass

