from src.helpers.files import load_txt_file
from src.year_2021.day_25.main import *

test_input = load_txt_file('./tests/year_2021/day_25/test_input.txt')

def test_q1():
    step = get_first_stationary_step(test_input)
    assert step == 58

def test_q2():
    pass