from src.helpers.files import load_txt_file

def run():
    input_rows = load_txt_file("./src/year_2021/day_2/input.txt")
    horizontal, depth = get_overall_movement(input_rows)
    print(f"Day 2 Q1: product of position = {horizontal * depth}")

    horizontal, depth = get_movement_with_aim(input_rows)
    print(f"Day 2 Q2: product of position = {horizontal * depth}")

def get_overall_movement(input_rows):
    horizontal = 0
    depth = 0
    for row in input_rows:
        direction, number = row.split()
        if direction == 'forward':
            horizontal += int(number)
        elif direction == 'up':
            depth -= int(number)
        elif direction == 'down':
            depth += int(number)
        else:
            raise Exception
    return horizontal, depth

def get_movement_with_aim(input_rows):
    horizontal = 0
    depth = 0
    aim = 0
    for row in input_rows:
        direction, number = row.split()
        if direction == 'forward':
            horizontal += int(number)
            depth += aim * int(number)
        elif direction == 'up':
            aim -= int(number)
        elif direction == 'down':
            aim += int(number)
        else:
            raise Exception
    return horizontal, depth