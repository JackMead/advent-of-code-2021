from src.helpers.files import load_txt_file
from enum import Enum
from itertools import permutations
from functools import total_ordering

unique_wire_counts = [2,3,4,7]

@total_ordering
class Position(Enum):
    TOP = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3
    CENTER = 4
    BOTTOM_LEFT = 5
    BOTTOM_RIGHT = 6
    BOTTOM = 7
    def __lt__(self, other):
        if self.__class__ is other.__class__:
           return self.value < other.value
        return NotImplemented

all_positions = [    
    Position.TOP,
    Position.TOP_LEFT,
    Position.TOP_RIGHT,
    Position.CENTER,
    Position.BOTTOM_LEFT,
    Position.BOTTOM_RIGHT,
    Position.BOTTOM
]


wires_per_num = {
    0: list(filter(lambda x: x != Position.CENTER, all_positions.copy())),
    1: [Position.TOP_RIGHT, Position.BOTTOM_RIGHT],
    2: [Position.TOP, Position.TOP_RIGHT, Position.CENTER, Position.BOTTOM_LEFT, Position.BOTTOM],
    3: [Position.TOP, Position.TOP_RIGHT, Position.CENTER, Position.BOTTOM_RIGHT, Position.BOTTOM],
    4: [Position.TOP_LEFT, Position.CENTER, Position.TOP_RIGHT, Position.BOTTOM_RIGHT],
    5: [Position.TOP, Position.TOP_LEFT, Position.CENTER, Position.BOTTOM_RIGHT, Position.BOTTOM],
    6: list(filter(lambda x: x != Position.TOP_RIGHT, all_positions.copy())),
    7: [Position.TOP, Position.TOP_RIGHT, Position.BOTTOM_RIGHT],
    8: all_positions.copy(),
    9: list(filter(lambda x: x != Position.BOTTOM_LEFT, all_positions.copy()))
}

numbers_per_length = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0,6,9],
    7: [8]
}

def run():
    inputs = load_txt_file('./src/day_8/input.txt')
    count = count_recognised_digits_easy(inputs)
    print(f"Day 8 Q1: There are {count} 1,4,7 & 8s in the output")
    total = sum_all_output_numbers(inputs)
    print(f"Day 8 Q2: The total of the outputs is {total}")


def count_recognised_digits_easy(inputs):
    total = sum([count_recognised_digits_for_one_line(input) for input in inputs])
    return total

def count_recognised_digits_for_one_line(input):
    info_string, outputs_string = input.split(' | ')
    outputs = outputs_string.split()
    total = sum([1 for out in outputs if len(out) in unique_wire_counts])
    return total

def sum_all_output_numbers(inputs):
    total = sum([get_output_for_one_line(input) for input in inputs])
    return total

def get_output_for_one_line(input):
    info_string, outputs_string = input.split(' | ')
    info = info_string.split()
    outputs = outputs_string.split()
    solution = solve_wires(info.copy() + outputs.copy())
    answer_string = "".join([get_value(output, solution) for output in outputs])
    return int(answer_string)

def solve_wires(wires):
    sorted_wires = sorted(wires)
    # assign a = position etc. test valid, then swap or 
    for p in permutations('abcdefg'):
        solution = {
            p[0]: Position.TOP,
            p[1]: Position.TOP_LEFT,
            p[2]: Position.TOP_RIGHT,
            p[3]: Position.CENTER,
            p[4]: Position.BOTTOM_LEFT,
            p[5]: Position.BOTTOM_RIGHT,
            p[6]: Position.BOTTOM
        }
        if solution_is_valid(sorted_wires, solution):
            return solution
    raise Exception("Nothing valid")

def solution_is_valid(sorted_wires, solution):
    for wire in sorted_wires:
        positions = [solution[char] for char in wire]
        length_of_wire = len(wire)
        possible_nums = numbers_per_length[length_of_wire]
        if sorted(positions) not in [sorted(wires_per_num[num]) for num in possible_nums]:
            return False
    return True

def get_value(output, solution):
    positions = [solution[char] for char in output]
    for num, pos in wires_per_num.items():
        if sorted(pos) == sorted(positions):
            return str(num)

'''
def first_pass():
        sorted_wires = [sorted(wire) for wire in wires]
    # dedupe
    sorted_wires = list(set(sorted_wires))

    starting = {
        'a': all_positions.copy(),
        'b': all_positions.copy(),
        'c': all_positions.copy(),
        'd': all_positions.copy(),
        'e': all_positions.copy(),
        'f': all_positions.copy(),
        'g': all_positions.copy()
    }

    for wire in sorted_wires:
        # remove positions if possible from each letter
        # e.g. abc means 7 = abc means defg do not contain top,top right, bottom right
        length = len(wire)
        possible_numbers = numbers_per_length[length]
        possible_positions = set(sum[wires_per_num(num) for num in possible_numbers]))

    # letter to position solution
    return {
        'a': Position.TOP_RIGHT
    }
'''