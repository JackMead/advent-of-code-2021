from src.helpers.files import load_txt_file
from src.day_10.main import score_corrupted_lines, score_incomplete_lines

test_input = load_txt_file('./tests/day_10/test_input.txt')

def test_q1():
    score = score_corrupted_lines(test_input)
    assert score == 26397

def test_q2():
    score = score_incomplete_lines(test_input)
    assert score == 288957