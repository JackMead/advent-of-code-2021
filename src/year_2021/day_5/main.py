from src.helpers.files import load_txt_file
from collections import Counter

def run():
    inputs = load_txt_file('./src/year_2021/day_5/input.txt')
    count = count_dangerous_areas_ignoring_diagonals(inputs)
    print(f"Day 5 Q1: There are {count} particularly dangerous areas")
    count = count_dangerous_areas_including_diagonals(inputs)
    print(f"Day 5 Q2: There are {count} particlarly dangerous areas")

class Vent():
    def __init__(self, input, diag_allowed = False):
        positions = input.split(' -> ')
        start = positions[0].split(',')
        end = positions[1].split(',')
        self.start_x = int(start[0])
        self.start_y = int(start[1])
        self.end_x = int(end[0])
        self.end_y = int(end[1])
        self.diag_allowed = diag_allowed

    @property
    def is_diagonal(self):
        return self.start_x != self.end_x and self.start_y != self.end_y

    @property
    def points_covered(self):
        if self.is_diagonal and not self.diag_allowed:
            return []
        if self.is_diagonal:
            start_y = max(self.start_y, self.end_y)
            direction = -1
            if (self.end_x > self.start_x) == (self.end_y > self.start_y):
                start_y = min(self.start_y, self.end_y)
                direction = 1
            big_x = max(self.start_x, self.end_x)
            little_x = min(self.start_x, self.end_x)
            big_y = max(self.start_y, self.end_y)
            little_y = min(self.start_y, self.end_y)
            return [(x, start_y + (direction * (x - little_x))) for x in range(little_x, big_x + 1)]
        if self.start_y == self.end_y:
            big = max(self.start_x, self.end_x)
            little = min(self.start_x, self.end_x)
            return [(x,self.end_y) for x in range(little, big + 1)]
        else:
            big = max(self.start_y, self.end_y)
            little = min(self.start_y, self.end_y)
            return [(self.end_x,y) for y in range(little, big + 1)]

    @property
    def to_input_format(self):
        return f"{self.start_x},{self.start_y} -> {self.end_x},{self.end_y}"

def count_dangerous_areas_ignoring_diagonals(inputs):
    vents = [Vent(input) for input in inputs]
    return count_dangerous_areas_for_vents(vents)

def count_dangerous_areas_including_diagonals(inputs):
    vents = [Vent(input, diag_allowed = True) for input in inputs]
    return count_dangerous_areas_for_vents(vents)

def count_dangerous_areas_for_vents(vents):
    all_points_covered = [point for vent in vents for point in vent.points_covered]
    counts = dict(Counter(all_points_covered))
    double_dangerous = 0
    for key, value in counts.items():
        if value >= 2:
            double_dangerous += 1
    return double_dangerous


'''
Helper functions used to diagnose issues
'''

def _print_grid_for_debugging(counts):
    row = ['.'] * 10
    grid = []
    for i in range(10):
        grid.append(row.copy())

    for key in counts:
        (x,y) = key
        grid[y][x] = str(counts[key])
    
    print()
    for row in grid:
        print(row)

def remove_diagonals(inputs):
    vents = [Vent(input) for input in inputs]
    non_diags = [vent.to_input_format for vent in vents if not vent.is_diagonal]
    with open('./src/year_2021/day_5/non_diags.txt', 'w') as file:
        file.write('\n'.join(non_diags))
    diags = [vent.to_input_format for vent in vents if vent.is_diagonal]
    with open('./src/year_2021/day_5/diags.txt', 'w') as file:
        file.write('\n'.join(diags))