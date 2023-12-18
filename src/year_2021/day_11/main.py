from src.helpers.files import load_txt_file
from src.helpers.coordinates import get_valid_adjacent_points_inc_diagonals

def run():
    input = load_txt_file('./src/year_2021/day_11/input.txt')
    count = count_flashes_after_100_steps(input)
    print(f"Day 11 Q1: {count} flashes")
    first_sim_flash = find_first_sim_flash(input)
    print(f"Day 11 Q2: first simultaneous flash is at step {first_sim_flash}")

class Octopus():
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False
        self.flash_count = 0

    def increment(self):
        if not self._is_overcharged():
            self.energy += 1

    def _is_overcharged(self):
        return self.energy > 9
    
    def flash(self):
        self.flashed = True

    def should_flash(self):
        return self.flashed == False and self._is_overcharged()

    def reset_if_flashing(self):
        if self._is_overcharged():
            self.energy = 0 
            self.flash_count += 1
            self.flashed = False


def count_flashes_after_100_steps(input):
    grid = read_into_grid(input)
    number_of_steps = 100
    for i in range (number_of_steps):
        iterate_grid(grid)
    return total_flash_count(grid)

def find_first_sim_flash(input):
    grid = read_into_grid(input)
    count = 0
    no_sim_flash = True
    while(no_sim_flash):
        no_sim_flash = was_no_simultaneous_flash(grid)
        count += 1
    return count

def was_no_simultaneous_flash(grid):
    iterate_grid(grid)
    return not all([oct.energy == 0 for row in grid for oct in row])


def iterate_grid(grid):
    increment_energy_initially(grid)
    overspill_energy_until_steady(grid)
    reset_flashers(grid)

def increment_energy_initially(grid):
    for row in grid:
        for oct in row:
            oct.increment()

def overspill_energy_until_steady(grid):
    changed = True
    while(changed):
        changed = overspill_energy_and_return_if_new_oct_ready(grid)
       

# Slighly overkill as the next octopus to be checked being ready still triggers another loop, but..
def overspill_energy_and_return_if_new_oct_ready(grid):
    go_again = False
    for row_index, row in enumerate(grid):
        for col_index, oct in enumerate(row):
            if oct.should_flash():
                oct.flash()
                coords = get_valid_adjacent_points_inc_diagonals(row_index, col_index, grid)
                for coord in coords:
                    new_oct = grid[coord.row][coord.col]
                    new_oct.increment()
                    if new_oct.should_flash():
                        go_again = True
    return go_again


def reset_flashers(grid):
    for row in grid:
        for oct in row:
            oct.reset_if_flashing()


def total_flash_count(grid):
    return sum([octopus.flash_count for row in grid for octopus in row])

def read_into_grid(input):
    grid = []
    for row in input:
        new_row = []
        for energy in row:
            starting_energy = int(energy)
            new_row.append(Octopus(starting_energy))
        grid.append(new_row)
    return grid