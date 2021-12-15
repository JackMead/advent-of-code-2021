from src.helpers.files import load_txt_file
from src.day_15.main import *

test_input = load_txt_file('./tests/day_15/test_input.txt')

def test_q1():
    path = shortest_weighted_path(test_input)
    assert path == 40

def test_q2():
    generate_bigger_test_input(test_input, './tests/day_15/generated_input.txt')
    generated_input = load_txt_file('./tests/day_15/generated_input.txt')
    given_input = load_txt_file('./tests/day_15/q2_test_input.txt')
    assert generated_input == given_input
    assert shortest_weighted_path(generated_input) == 315