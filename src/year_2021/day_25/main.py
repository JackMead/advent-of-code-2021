from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2021/day_25/input.txt')
    step = get_first_stationary_step(input)
    print(f"Day 25 Q1: stationary on step: {step}")

    print(f"Day 25 Q2: ")

def get_first_stationary_step(lines):
    grid = None
    new_grid = load_dicts(lines)
    count = 0
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1
    while (new_grid != grid):
        count += 1
        grid = new_grid
        new_grid = iterate_grid(grid, max_row, max_col)
        # display_grid(new_grid, max_row, max_col)
        # print(count)
        # if count >= 58:
        #     input()
    return count

def iterate_grid(grid, max_row, max_col):
    new_grid_after_east = {}
    for k, v in grid.items():
        row,col = k
        if v == '>':
            new_col = (col + 1) % (max_col + 1)
            if (row, new_col) not in grid:
                new_grid_after_east[(row, new_col)] = '>'
            else:
                new_grid_after_east[(row, col)] = '>'
        elif v == 'v':
            new_grid_after_east[(row, col)] = 'v'
    new_grid_after_south = {}
    
    for k, v in new_grid_after_east.items():
        row,col = k
        if v == '>':
            new_grid_after_south[(row, col)] = '>'
        elif v == 'v':
            new_row = (row + 1) % (max_row + 1)
            if (new_row, col) not in new_grid_after_east:
                new_grid_after_south[(new_row, col)] = 'v'
            else:
                new_grid_after_south[(row, col)] = 'v'
    return new_grid_after_south

def load_dicts(lines):
    grid = {}
    for row_idx in range(len(lines)):
        for col_idx in range(len(lines[0])):
            entry = lines[row_idx][col_idx]
            if entry != '.':
                grid[(row_idx, col_idx)] = entry
    return grid

def display_grid(grid, max_row, max_col):
    print()
    for row in range(max_row + 1):
        r = []
        for col in range(max_col + 1):
            if (row, col) in grid:
                r.append(grid[(row, col)])
            else:
                r.append('.')
        print(''.join(r))