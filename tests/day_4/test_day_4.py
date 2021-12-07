from src.day_4.main import get_winning_score
from src.helpers.files import load_txt_file

test_input = load_txt_file('./tests/day_4/test_input.txt')

def test_q1():
    score = get_winning_score(test_input)
    assert score == 4512