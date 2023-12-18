import sys
print("PATH:")
print(sys.path)
from src.helpers.files import load_txt_file
from src.year_2023.day_1.main import *

test_input = load_txt_file('./tests/year_2023/day_1/test_input.txt')

def test_q1():
    assert get_numbers_from_first_and_last_digits("1abc2") == 12
    assert get_numbers_from_first_and_last_digits("pqr3stu8vwx") == 38
    assert get_numbers_from_first_and_last_digits("a1b2c3d4e5f") == 15
    assert get_numbers_from_first_and_last_digits("treb7uchet") == 77

'''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

def test_q2():
    assert get_numbers_from_first_and_last_digits_inc_words("two1nine") == 29
    assert get_numbers_from_first_and_last_digits_inc_words("eightwothree") == 83
    assert get_numbers_from_first_and_last_digits_inc_words("abcone2threexyz") == 13
    assert get_numbers_from_first_and_last_digits_inc_words("xtwone3four") == 24
    assert get_numbers_from_first_and_last_digits_inc_words("4nineeightseven2") == 42
    assert get_numbers_from_first_and_last_digits_inc_words("zoneight234") == 14
    assert get_numbers_from_first_and_last_digits_inc_words("7pqrstsixteen") == 76