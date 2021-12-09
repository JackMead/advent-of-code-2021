from src.day_8.main import count_recognised_digits_easy, sum_all_output_numbers, get_value, solve_wires, solution_is_valid, Position
from src.helpers.files import load_txt_file

test_input = load_txt_file('./tests/day_8/test_input.txt')

def test_q1():
    count = count_recognised_digits_easy(test_input)
    assert count == 26

def test_q2():
    total = sum_all_output_numbers(test_input)
    assert total == 61229

def test_get_value():
    pass

def test_solve_wires():
    pass

def test_solution_is_valid():
    first_input = test_input[0]
    valid_solution = {
        'd': Position.TOP,
        'c': Position.CENTER,
        'g': Position.TOP_LEFT,
        'f': Position.BOTTOM,
        'a': Position.BOTTOM_LEFT,
        'b': Position.TOP_RIGHT,
        'e': Position.BOTTOM_RIGHT
    }
    info_string, outputs_string = first_input.split(' | ')
    info = info_string.split()
    outputs = outputs_string.split()
    wires = sorted(info + outputs)
    assert solution_is_valid(wires, valid_solution)