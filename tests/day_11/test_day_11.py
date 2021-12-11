from src.helpers.files import load_txt_file
from src.day_11.main import *

test_input = load_txt_file('./tests/day_11/test_input.txt')

def test_q1():
    count = count_flashes_after_100_steps(test_input)
    assert count == 1656

def test_q2():
    timer = find_first_sim_flash(test_input)
    assert timer == 195