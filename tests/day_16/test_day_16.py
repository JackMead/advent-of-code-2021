from src.helpers.files import load_txt_file
from src.day_16.main import *

test_input = load_txt_file('./tests/day_16/test_input.txt')
test_input_2 = load_txt_file('./tests/day_16/test_input_2.txt')

def test_q1():
    expected_sums = [6, 14, 16,23, 31, 12]
    # -1 as final test example is failing, but seems to be dodgy data?
    for i in range(len(test_input)):
        line = test_input[i]
        version_sum = sum_packet_versions(line)
        assert version_sum == expected_sums[i]

def test_broken_case():
    sum = 12
    line = test_input[5]
    version_sum = sum_packet_versions(line)
    assert version_sum == sum

def test_q2_broken_case():
    packet_value = 54
    case = '04005AC33890'
    value = get_packet_value(case)
    assert value == packet_value


def test_q2():
    expected_value = [3, 54, 7, 9, 1, 0, 0, 1]
    # -1 as final test example is failing, but seems to be dodgy data?
    for i in range(len(test_input_2)):
        line = test_input_2[i]
        value = get_packet_value(line)
        assert value == expected_value[i]