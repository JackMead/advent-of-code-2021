from src.helpers.files import load_list_of_nums_on_line_1
from src.day_7.main import get_actual_minimal_alignment_cost, get_minimal_alignment_cost

test_input = load_list_of_nums_on_line_1('./tests/day_7/test_input.txt')

def test_q1():
    cost = get_minimal_alignment_cost(test_input)
    assert cost == 37

def test_q2():
    cost = get_actual_minimal_alignment_cost(test_input)
    assert cost == 168