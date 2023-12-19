from src.helpers.coordinates import get_valid_adjacent_points_inc_diagonals
from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2023/day_3/input.txt')
    parsed = parse_input(input)
    sum = sum_of_part_numbers(parsed)

    print(f"Day 3 Q1: {sum}")

    sum = sum_of_gear_ratios(parsed)
    print(f"Day 3 Q2: {sum}")

def parse_input(input):
    return input

def sum_of_gear_ratios(input):
    sum = 0
    for row_index in range(len(input)):
        row = input[row_index]
        for col_index in range(len(row)):
            if row[col_index] == '*':
                adjacent_numbers = []
                neighbours = get_valid_adjacent_points_inc_diagonals(row_index, col_index, input)
                for neighbour in neighbours:
                    if input[neighbour.row][neighbour.col].isnumeric():
                        adjacent_numbers.append(get_number(input, neighbour))
                deduped = list(set(adjacent_numbers))
                # THIS ASSUMES THAT A GEAR NEVER GENUINELY TOUCHES THE SAME NUMBER TWICE - BAD ASSUMPTION BUT WORKS
                if len(deduped) == 2:
                    sum += int(deduped[0]) * int(deduped[1])
                elif len(deduped) > 2:
                    print(f"Position row: {row_index}, col: {col_index} touches 3+ numbers?")

    return sum

def get_number(input, coord):
    row = coord.row
    col = coord.col
    while col > 0:
        if input[row][col - 1].isnumeric():
            col -= 1
        else: break
    number = input[row][col]

    while col < len(input[0]) - 1:
        if input[row][col + 1].isnumeric():
            col += 1
            number += input[row][col]
        else:
            break
    return number


def sum_of_part_numbers(input):
    sum = 0
    for row_index in range(len(input)):
        row = input[row_index]
        current_number = ''
        for col_index in range(len(row)):
            if row[col_index].isnumeric():
                current_number += row[col_index]
                if col_index == len(input[0]) - 1:
                    if check_if_valid(input, current_number, row_index, col_index + 1 - len(current_number)):
                        # print(f"FINAL col: {current_number}")
                        sum += int(current_number)
                    # else:
                        # print(f"Number {current_number} ain't valid")
            else:
                if current_number != '':
                    if check_if_valid(input, current_number, row_index, col_index - len(current_number)):
                        sum += int(current_number)
                    # else:
                        # print(f"Number {current_number} ain't valid")
                current_number = ''
    return sum

def check_if_valid(input_grid, number, row_index, col_index_of_start):
    length = len(number)
    one_left = max(col_index_of_start - 1, 0)
    num_cols = len(input_grid[0])
    one_right = min(col_index_of_start + length, num_cols - 1)
    # print(number)
    # print(col_index_of_start)
    # print(one_left)
    # print(one_right)
    if row_index > 0:
        for i in range(one_left, one_right + 1):
        #   FOR NOW ASSUME A NUMBER IS A SYMBOL?
            if input_grid[row_index - 1][i] != '.':
                return True
    if row_index < len(input_grid) - 1:
        for i in range(one_left, one_right + 1):
        #   FOR NOW ASSUME A NUMBER IS A SYMBOL?
            if input_grid[row_index + 1][i] != '.':
                return True
    if col_index_of_start > 0:
        if input_grid[row_index][col_index_of_start - 1] != '.':
            return True
    if col_index_of_start + length < num_cols:
        if input_grid[row_index][col_index_of_start + length] != '.':
            return True
    return False

        
