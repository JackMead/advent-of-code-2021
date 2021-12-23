from src.helpers.files import load_txt_file
from src.day_23.main import *

test_input = load_txt_file('./tests/day_23/test_input.txt')
test_input_2 = load_txt_file('./tests/day_23/test_input_2.txt')
finished_input = load_txt_file('./tests/day_23/finished_input.txt')

def test_finished_input_returns_0():
    energy = get_energy_required_to_organise(finished_input)
    assert energy == 0

def test_valid_path():
    g = get_default_graph()
    g.nodes['h']['occupied'] = 'D'
    path = ['h','i', 'r', 's']
    assert is_valid_path(g.nodes['h'], path, g)
    g.nodes['h'].pop('occupied')
    g.nodes['s']['occupied'] = 'D'
    
    g.nodes['f']['occupied'] = 'D'
    path = ['f', 'h','i', 'r']
    assert is_valid_path(g.nodes['f'], path, g)

def test_simple_swap():
    energy = get_energy_required_to_organise(test_input_2)
    assert energy == 4646

def test_q1():
    energy = get_energy_required_to_organise(test_input)
    assert energy == 12521

def test_q2():
    energy = get_full_energy_required_to_organise(test_input)
    assert energy == 44169