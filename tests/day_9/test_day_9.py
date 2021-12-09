from src.helpers.files import load_txt_file
from src.day_9.main import sum_risk_scores

test_input = load_txt_file('./tests/day_9/test_input.txt')

def test_q1():
    score = sum_risk_scores(test_input)
    assert score == 15