from typing import List

import pytest
from src.random.data_annotation_pipes import find_sinks, load_input

def test_pipes():
    input = load_input("./src/random/input_1.txt")
    
    sinks = find_sinks(input)

    assert sinks == "AC"


# @pytest.mark.skip()
def test_pipes_2():
    input = load_input("./src/random/input_2.txt")
    
    sinks = find_sinks(input)

    assert sinks == "AC"
