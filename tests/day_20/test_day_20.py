from src.helpers.files import load_txt_file
from src.day_20.main import *
import pytest

test_input = load_txt_file('./tests/day_20/test_input.txt')

def test_q1():
    count = count_lights_after_two_enhancements(test_input)
    assert count == 35

@pytest.mark.skip(reason = "Slow")
def test_q2():
    count = count_lights_after_50_enhancements(test_input)
    assert count == 3351