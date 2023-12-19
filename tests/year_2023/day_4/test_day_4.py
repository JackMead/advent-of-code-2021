from src.helpers.files import load_txt_file
from src.year_2023.day_4.main import *

test_input = load_txt_file('./tests/year_2023/day_4/test_input.txt')

def test_q1():
    scores = [score_card(card) for card in test_input]
    assert scores == [8,2,2,1,0,0]

def test_q2():
    assert count_total_scratchcards(test_input) == 30