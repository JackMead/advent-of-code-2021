from src.helpers.files import load_txt_file
from src.year_2021.day_18.main import *
import pytest

test_input = load_txt_file('./tests/year_2021/day_18/test_input.txt')
test_input_2 = load_txt_file('./tests/year_2021/day_18/test_input_2.txt')

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

def test_more_additions():
    n1 = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    n2 = [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
    n3 = [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
    n4 = [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
    n5 = [7,[5,[[3,8],[1,4]]]]
    n6 = [[2,[2,2]],[8,[8,1]]]
    n7 = [2,9]
    n8 = [1,[[[9,3],9],[[9,0],[0,7]]]]
    n9 = [[[5,[7,4]],7],1]
    n10 = [[[[4,2],2],6],[8,7]]
    running_total = add_nums(n1, n2)
    assert running_total == [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    running_total = add_nums(running_total, n3)
    assert running_total == [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
    running_total = add_nums(running_total, n4)
    assert running_total == [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
    running_total = add_nums(running_total, n5)
    assert running_total == [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
    running_total = add_nums(running_total, n6)
    assert running_total == [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
    running_total = add_nums(running_total, n7)
    assert running_total == [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
    running_total = add_nums(running_total, n8)
    assert running_total == [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
    running_total = add_nums(running_total, n9)
    assert running_total == [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
    running_total = add_nums(running_total, n10)
    assert running_total == [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]

def test_more():
    magnitude = get_magnitude_of_sum(test_input_2)
    expected_ans = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
    assert magnitude == get_magnitude(expected_ans)

def test_q1():
    magnitude = get_magnitude_of_sum(test_input)
    assert magnitude == 4140

def test_q2():
    max_mag = get_max_magnitude_of_sum(test_input)
    assert max_mag == 3993