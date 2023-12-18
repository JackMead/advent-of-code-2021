from src.helpers.files import load_txt_file
from functools import reduce

def run():
    input = load_txt_file('./src/year_2021/day_9/input.txt')
    risk_score_total = sum_risk_scores(input)
    print(f"Day 9 Q1: Total risk score = {risk_score_total}")
    basin_score = total_basin_score(input)
    print(f"Day 9 Q2: Total basin score = {basin_score}")

def sum_risk_scores(input):
    grid = build_grid(input)
    low_points = find_low_points(grid)
    height_of_low_points = get_height_of_low_points(low_points)
    risk_scores = get_risk_scores(height_of_low_points)
    return sum(risk_scores)

def total_basin_score(input):
    grid = build_grid(input)
    low_points = find_low_points(grid)
    basin_sizes = [get_size_of_basin_for_low_point(low_point, grid) for low_point in low_points]
    three_largest_basins = sorted(basin_sizes)[-3:]
    return reduce((lambda x, y: x * y), three_largest_basins)

count = -1
def get_size_of_basin_for_low_point(low_point, grid):
    points_seen = [low_point]
    queue = points_seen.copy()

    while len(queue) > 0:
        point = queue.pop(0)
        points_to_compare = []
        add_point_if_valid(points_to_compare, point.row, point.col - 1, grid)
        add_point_if_valid(points_to_compare, point.row, point.col + 1, grid)
        add_point_if_valid(points_to_compare, point.row - 1, point.col, grid)
        add_point_if_valid(points_to_compare, point.row + 1, point.col, grid)
        for point_to_check in points_to_compare:
            if point_to_check not in points_seen and point_to_check.height < 9:
                points_seen.append(point_to_check)
                queue.append(point_to_check)
    return len(points_seen)

class InvalidPointException(Exception):
    pass

class Point():
    def __init__(self, row, col, grid):
        if not point_is_valid(row, col, grid):
            raise InvalidPointException()
        self.row = row
        self.col = col
        self.height = grid[row][col]

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

def find_low_points(grid):
    low_points = []
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            point = Point(row_index, col_index, grid)
            if surroundings_higher(point, grid):
                low_points.append(point)
    return low_points

def surroundings_higher(point, grid):
    points_to_compare = []
    add_point_if_valid(points_to_compare, point.row, point.col - 1, grid)
    add_point_if_valid(points_to_compare, point.row, point.col + 1, grid)
    add_point_if_valid(points_to_compare, point.row - 1, point.col, grid)
    add_point_if_valid(points_to_compare, point.row + 1, point.col, grid)

    for adjacent_point in points_to_compare:
        if adjacent_point.height <= point.height:
            return False
    return True

def add_point_if_valid(array, row, col, grid):
    try:
        new_point = Point(row, col, grid)
        array.append(new_point)
    except:
        pass

def point_is_valid(row, col, grid):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

def build_grid(input):
    grid = []
    
    for row in input:
        new_row = []
        for char in row:
            new_row.append(int(char))
        grid.append(new_row)
    return grid

def get_height_of_low_points(low_points):
    return [point.height for point in low_points]

def get_risk_scores(height_of_low_points):
    return [height + 1 for height in height_of_low_points]