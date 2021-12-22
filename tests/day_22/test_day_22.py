from src.helpers.files import load_txt_file
from src.day_22.main import *
import pytest

test_input = load_txt_file('./tests/day_22/test_input.txt')
test_input_2 = load_txt_file('./tests/day_22/test_input_2.txt')

def test_q1():
    count = count_active_in_initialisation_region(test_input)
    assert count == 590784

@pytest.mark.skip(reason = "This test is designed to be slow but informative!")
def test_brute():
    count = count_active_everywhere_brute(test_input_2)
    assert count == 2758514936282235

def test_q2_approach():
    simple_input = [
        "on x=0..2,y=0..2,z=0..2", 
        "off x=0..1,y=0..0,z=0..0",
        "on x=0..1,y=0..1,z=0..1"]
    count_correct = count_active_in_initialisation_region(simple_input)
    count = count_active_everywhere(simple_input)
    assert count == count_correct

def test_q2():
    count = count_active_in_initialisation_region(test_input_2)
    assert count == 474140
    count = count_active_everywhere(test_input_2)
    assert count == 2758514936282235