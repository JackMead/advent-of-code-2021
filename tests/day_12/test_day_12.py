from src.helpers.files import load_txt_file
from src.day_12.main import *

test_input_1 = load_txt_file('./tests/day_12/test_input_1.txt')
test_input_2 = load_txt_file('./tests/day_12/test_input_2.txt')
test_input_3 = load_txt_file('./tests/day_12/test_input_3.txt')

def test_q1():
    count_1 = count_paths_through_caves(test_input_1)
    assert count_1 == 10
    count_2 = count_paths_through_caves(test_input_2)
    assert count_2 == 19
    count_3 = count_paths_through_caves(test_input_3)
    assert count_3 == 226

def test_q2():
    count_1 = count_paths_through_caves_allowing_repeat(test_input_1)
    assert count_1 == 36
    count_2 = count_paths_through_caves_allowing_repeat(test_input_2)
    assert count_2 == 103
    count_3 = count_paths_through_caves_allowing_repeat(test_input_3)
    assert count_3 == 3509