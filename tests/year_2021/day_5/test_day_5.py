from src.year_2021.day_5.main import count_dangerous_areas_including_diagonals, count_dangerous_areas_ignoring_diagonals, Vent
from src.helpers.files import load_txt_file

test_input = load_txt_file('./tests/year_2021/day_5/test_input.txt')

def test_creating_vent_works():
    vent = Vent(test_input[0])
    assert vent.start_x == 0
    assert vent.start_y == 9
    assert vent.end_x == 5
    assert vent.end_y == 9
    assert not vent.is_diagonal

def test_vent_with_inverted_y_made_correctly():
    vent = Vent("343,710 -> 343,96")
    assert vent.start_x == 343
    assert vent.start_y == 710
    assert vent.end_x == 343
    assert vent.end_y == 96
    assert not vent.is_diagonal

def test_diagonals_work():
    vent = Vent(test_input[5])
    assert vent.start_x == 6
    assert vent.start_y == 4
    assert vent.end_x == 2
    assert vent.end_y == 0
    assert vent.is_diagonal
    assert vent.points_covered == []

def test_vent_covering_works():
    vent = Vent(test_input[0])
    assert vent.points_covered == [(0,9), (1,9), (2,9), (3,9), (4,9), (5,9)]

def test_vent_diagonal_covering_works():
    vent = Vent(test_input[1], diag_allowed = True)
    assert vent.points_covered == [(0,8), (1,7), (2,6), (3,5), (4,4), (5,3), (6,2), (7,1), (8,0)]

def test_q1():
    count = count_dangerous_areas_ignoring_diagonals(test_input)
    assert count == 5

def test_q2():
    count = count_dangerous_areas_including_diagonals(test_input)
    assert count == 12
