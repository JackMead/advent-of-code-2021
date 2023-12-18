from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2021/day_15/input.txt')
    path = shortest_weighted_path(input)
    print(f"Day 15 Q1: risk level = {path}")
    generated_filepath = './src/year_2021/day_15/generated.txt'
    generate_bigger_test_input(input, generated_filepath)
    updated_input = load_txt_file(generated_filepath)
    path = shortest_weighted_path(updated_input)
    print(f"Day 15 Q2: risk level = {path}")

def generate_bigger_test_input(input, filepath):
    grid = generate_bigger_grid(input)
    with open(filepath, 'w') as file:
        for row in grid:
            file.write("".join([str(num) for num in row]))
            file.write('\n')

def wrapped_num(num):
    if num <= 9:
        return num
    else:
        return num - 9

def generate_bigger_grid(input):
    # append rows
    grid = input.copy()
    for i in range (1,5):
        for row in input:
            new_row = [wrapped_num(int(num) + i) for num in row]
            grid.append(new_row)

    vertical_snapshot = copy_grid(grid)

    for i in range(1,5):
        for row_index in range(len(vertical_snapshot)):
            new_cols = [str(wrapped_num(int(num) + i)) for num in vertical_snapshot[row_index]]
            new_cols_string = "".join(new_cols)
            grid[row_index] += new_cols_string
    return grid

def shortest_weighted_path(input):
    grid = read_input_to_grid(input)
    cumulative_risks = get_cumulative_risks(grid)
    return get_shortest_cumulative_risk(cumulative_risks)

def copy_grid(grid):
    copy = []
    for row in grid:
        new_row = []
        for col in row:
            new_row.append(col)
        copy.append(new_row)
    return copy


def get_cumulative_risks(grid):
    height = len(grid)
    width = len(grid[0])
    big_number = height * width
    cumulative_risks = [[None] * width for i in range(height)]
    cumulative_risks[height-1][width-1] = grid[height-1][width -1]
    for i in range (big_number):
        old_risks = copy_grid(cumulative_risks)
        for y in range(height-1, -1, -1):
            for x in range(width-1, -1, -1):
                shortest_neighbour = get_shortest_surrounding_path(cumulative_risks, x, y)
                if not shortest_neighbour:
                    continue
                squares_risk = grid[y][x]
                new_comparison = shortest_neighbour + squares_risk
                existing_path = cumulative_risks[y][x]
                if (not existing_path) or new_comparison < existing_path:
                    cumulative_risks[y][x] = new_comparison
        if grids_match(old_risks, cumulative_risks):
            print(f"Ending early: {i + 1} iterations complete")
            break

    return cumulative_risks

def grids_match(grid_1, grid_2):
    for row_index in range(len(grid_1)):
        for col_index in range(len(grid_1[0])):
            if grid_1[row_index][col_index] != grid_2[row_index][col_index]:
                return False
    return True

def get_shortest_surrounding_path(grid, x, y):
    height = len(grid)
    width = len(grid[0])
    positions = [
        (x, y+1),
        (x, y-1),
        (x+1, y),
        (x-1, y)
    ]
    shortest = None
    for position in positions:
        if position[0] < 0 or position[0] >= width or position[1] < 0 or position[1] >= height:
            continue
        value = grid[position[1]][position[0]]
        if (value != None) and ((shortest == None) or (value < shortest)):
            shortest = value
    return shortest

def get_shortest_cumulative_risk(grid):
    # ignore risk score of start in top left
    return min(grid[0][1], grid[1][0])

def read_input_to_grid(input):
    grid = []
    for line in input:
        new_row = []
        for num in line:
            new_row.append(int(num))
        grid.append(new_row)
    return grid

def display_grid(grid):
    for row in grid:
        print(" ".join([str(num) for num in row]))

    print()