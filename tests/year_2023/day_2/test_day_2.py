from src.helpers.files import load_txt_file
from src.year_2023.day_2.main import *

test_input = load_txt_file('./tests/year_2023/day_2/test_input.txt')

def test_q1():
    games = parse_games(test_input)

    assert is_possible(games[0]) == True
    assert is_possible(games[1]) == True
    assert is_possible(games[2]) == False
    assert is_possible(games[3]) == False
    assert is_possible(games[4]) == True

def test_q2():
    games = parse_games(test_input)

    assert power_of_game(games[0]) == 48
    assert power_of_game(games[1]) == 12
    assert power_of_game(games[2]) == 1560
    assert power_of_game(games[3]) == 630
    assert power_of_game(games[4]) == 36