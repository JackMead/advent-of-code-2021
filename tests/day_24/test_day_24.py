from src.helpers.files import load_txt_file
from src.day_24.main import *

test_input = load_txt_file('./tests/day_24/test_input.txt')
test_input_2 = load_txt_file('./tests/day_24/test_input_2.txt')

def test_q1():
    instructions = parse_lines(test_input)
    assert not is_valid_monad('13', instructions)
    reset_cache()
    assert is_valid_monad('14', instructions)
    reset_cache()
    
    instructions = parse_lines(test_input_2)
    assert not is_valid_monad('9', instructions)
    reset_cache()
    assert is_valid_monad('6', instructions)

def test_q2():
    pass