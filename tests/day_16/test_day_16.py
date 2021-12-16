from src.helpers.files import load_txt_file
from src.day_16.main import *

test_input = load_txt_file('./tests/day_16/test_input.txt')

def test_q1():
    expected_sums = [6, 16, 12, 23, 31]
    for i in range(len(test_input)):
        line = test_input[i]
        version_sum = sum_packet_versions(line)
        assert version_sum == expected_sums[i]
        print(version_sum)

def test_q2():
    pass