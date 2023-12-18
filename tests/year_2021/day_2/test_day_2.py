from src.year_2021.day_2.main import get_overall_movement, get_movement_with_aim

q1_example = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

def test_q1():
    horizontal, depth = get_overall_movement(q1_example)
    assert horizontal == 15
    assert depth == 10

def test_q2():
    horizontal, depth = get_movement_with_aim(q1_example)
    assert horizontal == 15
    assert depth == 60
