from src.helpers.files import load_txt_file
from src.year_2023.day_3.main import *

test_input = load_txt_file('./tests/year_2023/day_3/test_input.txt')

def test_q1():
    input = parse_input(test_input)

    assert sum_of_part_numbers(input) == 4361

def test_q2():
    input = parse_input(test_input)

    assert sum_of_gear_ratios(input) == 467835