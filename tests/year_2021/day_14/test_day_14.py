from src.helpers.files import load_txt_file
from src.year_2021.day_14.main import *

test_input = load_txt_file('./tests/year_2021/day_14/test_input.txt')

def test_q1():
    range = get_range_of_element_counts_at_step_X(test_input, 10)
    assert range == 1588
    range = get_range_of_element_counts_at_step_X_efficient(test_input, 10)
    assert range == 1588

def test_q2():
    range = get_range_of_element_counts_at_step_X_efficient(test_input, 40)
    assert range == 2188189693529