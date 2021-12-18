from src.helpers.files import load_txt_file
from src.day_18.main import *

test_input = load_txt_file('./tests/day_18/test_input.txt')

def test_simple_addition():
    running_total = add_nums([1,1], [2,2])
    running_total = add_nums(running_total, [3,3])
    total = add_nums(running_total, [4,4])
    assert total == [[[[1,1],[2,2]],[3,3]],[4,4]]

def test_magnitude():
    mag = get_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
    assert mag == 3488

def test_reduction():
    reduced = reduce_num([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
    print(reduced)
    assert reduced == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

def test_q1():
    magnitude = get_magnitude_of_sum(test_input)
    assert magnitude == 4140

def test_q2():
    pass