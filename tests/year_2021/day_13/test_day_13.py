from src.helpers.files import load_txt_file
from src.year_2021.day_13.main import *

test_input = load_txt_file('./tests/year_2021/day_13/test_input.txt')

def test_q1():
    count = count_dots_after_one_fold(test_input)
    assert count == 17

def test_q2():
    print()
    # Asserts on length, but square shape can also be checked by eye
    points = print_output_of_all_folds(test_input)
    assert points == 16