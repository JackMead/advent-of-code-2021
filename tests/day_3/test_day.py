from src.day_3.main import get_gamma_and_epsilon

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

def test_q1():
    gamma, epsilon = get_gamma_and_epsilon(test_input)
    assert gamma == 22
    assert epsilon == 9

def test_q2():
    pass