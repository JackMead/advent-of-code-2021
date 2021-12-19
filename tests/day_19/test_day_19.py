from src.helpers.files import load_txt_file
from src.day_19.main import *

test_input = load_txt_file('./tests/day_19/test_input.txt')

def test_q1():
    count = count_beacons(test_input)
    assert count == 79

def test_q2():
    pass