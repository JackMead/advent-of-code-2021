from src.helpers.files import load_txt_file
from collections import Counter

def run():
    inputs = load_txt_file('./src/day_5/input.txt')
    count = count_dangerous_areas_ignoring_diagonals(inputs)
    print(f"Day 5 Q1: There are {count} particularly dangerous areas")

class Vent():
    def __init__(self, input):
        positions = input.split(' -> ')
        start = positions[0].split(',')
        end = positions[1].split(',')
        self.start_x = int(min(start[0], end[0]))
        self.start_y = int(min(start[1], end[1]))
        self.end_x = int(max(start[0],end[0]))
        self.end_y = int(max(start[1],end[1]))

    @property
    def is_diagonal(self):
        return self.start_x != self.end_x and self.start_y != self.end_y

    @property
    def points_covered(self):
        if self.is_diagonal:
            return []
        if self.start_y == self.end_y:
            return [(x,self.end_y) for x in range(self.start_x, self.end_x + 1)]
        else:
            return [(self.end_x,y) for y in range(self.start_y, self.end_y + 1)]

def count_dangerous_areas_ignoring_diagonals(inputs):
    vents = [Vent(input) for input in inputs]
    print(len(vents))
    all_points_covered = [point for vent in vents for point in vent.points_covered]
    print(len(all_points_covered))
    counts = dict(Counter(all_points_covered))
    # _print_grid_for_debugging(counts)
    double_dangerous = 0
    for key, value in counts.items():
        if value >= 2:
            # print(key)
            double_dangerous += 1
    return double_dangerous

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