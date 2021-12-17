from src.helpers.files import load_txt_file
from src.day_17.main import *

test_input = load_txt_file('./tests/day_17/test_input.txt')

def test_target_class():
    target = Target(test_input[0])
    assert target.min_x == 20
    assert target.max_x == 30
    assert target.min_y == -10
    assert target.max_y == -5

def test_q1():
    max_y = find_max_y_position_reaching_target(test_input[0])
    assert max_y == 45

def test_q2():
    count = count_distinct_velocities(test_input[0])
    assert count == 112