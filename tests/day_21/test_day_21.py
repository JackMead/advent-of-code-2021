from src.helpers.files import load_txt_file
from src.day_21.main import *

test_input = load_txt_file('./tests/day_21/test_input.txt')

def test_q1():
    points = get_loser_points(test_input, DeterministicDie(100))
    assert points == 739785

def test_q2():
    winners = get_winning_universes(test_input)
    assert winners == 444356092776315