from src.day_4.main import get_winning_score, get_boards, get_numbers, is_board_finished, mark_number
from src.helpers.files import load_txt_file

test_input = load_txt_file('./tests/day_4/test_input.txt')

def test_get_numbers():
    numbers = get_numbers(test_input)
    assert len(numbers) == 27
    assert numbers[0] == 7
    assert numbers[10] == 21
    assert numbers[26] == 1

def test_get_board():
    boards = get_boards(test_input)
    assert len(boards) == 3
    assert len(boards[0]) == 5
    assert len(boards[0][0]) == 5

def test_is_board_finished_true_for_finished_row():
    board = [[1,2], ['*', '*']]
    assert is_board_finished(board)

def test_is_board_finished_true_for_finished_col():
    board = [['*',2], ['*', 3]]
    assert is_board_finished(board)

def test_is_board_finished_false_otherwise():
    board = [['*',2], [3, '*']]
    assert not is_board_finished(board)

def test_mark_number():
    board = [[1,2], [3,4]]
    mark_number([board], 3)
    assert board[1][0] == '*'

def test_q1():
    score = get_winning_score(test_input)
    assert score == 4512