from src.day_6.main import count_lantern_fish_after_days
from src.day_6.main import load_txt_file

test_input = load_txt_file('./tests/day_6/test_input.txt')

def test_q1():
    number_after_18_days = count_lantern_fish_after_days(test_input[0], 18)
    assert number_after_18_days == 26
    number_after_80_days = count_lantern_fish_after_days(test_input[0], 80)
    assert number_after_80_days == 5934

def test_q2():
    number_after_many_days = count_lantern_fish_after_days(test_input[0], 256)
    assert number_after_many_days == 26984457539
    

def test_one_fish_one_day():
    number = count_lantern_fish_after_days('1', 1)
    assert number == 1

def test_fish_about_to_spawn():
    number = count_lantern_fish_after_days('0', 1)
    assert number == 2