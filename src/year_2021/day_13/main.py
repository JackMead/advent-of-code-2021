from src.helpers.files import load_txt_file
from src.helpers.coordinates import Coordinate

def run():
    input = load_txt_file('./src/year_2021/day_13/input.txt')
    count = count_dots_after_one_fold(input)
    print(f"Day 13 Q1: {count} dots after one fold")
    print(f"Day 13 Q2: ")
    print_output_of_all_folds(input)

def count_dots_after_one_fold(input):
    points, folds = read_input(input)
    new_points = perform_fold(folds[0], points)
    return len(new_points)

def get_output_of_all_folds(input):
    points, folds = read_input(input)
    for fold in folds:
        points = perform_fold(fold, points)
    return points

def print_output_of_all_folds(input):
    points = get_output_of_all_folds(input)
    display_points(points)
    return len(points)

class Fold():
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value

def perform_fold(fold, points):
    new_points = []
    if fold.axis == 'y':
        for point in points:
            if point.row < fold.value:
                new_points.append(point)
            else:
                new_row = fold.value - (point.row - fold.value)
                new_points.append(Coordinate(new_row ,point.col))
    elif fold.axis == 'x':
        for point in points:
            if point.col < fold.value:
                new_points.append(point)
            else:
                new_col = fold.value - (point.col - fold.value)
                new_points.append(Coordinate(point.row, new_col))
    else:
        raise Exception(f"Unknown axis: {fold.axis}")
    return set(new_points)

def read_input(lines):
    lines_for_dots = [line.split(',') for line in lines if ',' in line]
    dots = [Coordinate(int(line[1]), int(line[0])) for line in lines_for_dots]
    lines_for_folds = [line[11:].split('=') for line in lines if line.startswith('fold along ')]
    folds = [Fold(line[0], int(line[1])) for line in lines_for_folds]
    return set(dots), folds

def display_points(points):
    max_row = max([point.row for point in points])
    max_col = max([point.col for point in points])

    for r in range(max_row + 1):
        row = []
        for c in range(max_col + 1):
            if Coordinate(r, c) in points:
                row.append('#')
            else:
                row.append('.')
        print("".join(row))