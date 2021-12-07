from src.day_1.main import count_number_of_increases, count_number_of_increases_with_sliding_window

def test_q1():
    nums = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]
    assert count_number_of_increases(nums) == 7

def test_q2():
    nums = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]
    assert count_number_of_increases_with_sliding_window(nums) == 5