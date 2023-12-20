from src.helpers.files import load_txt_file
from src.year_2023.day_5.main import *

test_input = load_txt_file('./tests/year_2023/day_5/test_input.txt')

def test_q1():
    parsed = parse_input(test_input)

    nearest_valid_location = find_nearest_valid_location(parsed)

    assert nearest_valid_location == 35

def test_q2():
    parsed = parse_input(test_input)

    nearest_valid_location = find_nearest_valid_location(parsed, part_two=True)

    assert nearest_valid_location == 46