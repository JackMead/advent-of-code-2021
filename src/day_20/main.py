from src.helpers.files import load_txt_file
from src.helpers.debug import print_grid_symbols
from src.helpers.perf import add_profile

def run():
    input = load_txt_file('./src/day_20/input.txt')
    count = count_lights_after_two_enhancements(input)
    print(f"Day 20 Q1: There are {count} light pixels")
    count = count_lights_after_50_enhancements(input)
    print(f"Day 20 Q2: There are {count} light pixels after many enhancements")

are_all_lit = False

def count_lights_after_two_enhancements(input):
    algorithm, input_image = parse_input(input)

    # print_grid_symbols(input_image)
    output_image = enhance(input_image, algorithm)
    output_image = enhance(output_image, algorithm)

    count = count_lights_in_image(output_image)
    return count

def count_lights_after_50_enhancements(input):
    algorithm, input_image = parse_input(input)

    running_image = input_image
    for i in range(50):
        running_image = enhance(running_image, algorithm)

    count = count_lights_in_image(running_image)
    return count


def parse_input(input):
    algorithm = input[0]
    # extend the image by n layer of dots all round - anything outside this will remain dots
    # relies on max n enhancements taking place
    extra_padding = 55
    image = []
    for line in input[2:]:
        row = []
        for i in range(extra_padding):
            row.append('.')
        row.extend([c for c in line])
        for i in range(extra_padding):
            row.append('.')
        image.append(row)
    line_length = len(image[0])
    for i in range(extra_padding):
        new_line = ['.'] * line_length
        new_line_2 = ['.'] * line_length
        image.append(new_line)
        image.insert(0, new_line_2)
    return algorithm, image


def enhance(image, algorithm):
    new_image = []
    global are_all_lit
    
    for row_index in range(len(image)):
        new_row = []
        for col_index in range(len(image[0])):
            bin_string = get_surrounding_squares_in_binary(image, row_index, col_index)
            bin_num = int(bin_string, 2)
            symbol = algorithm[bin_num]
            new_row.append(symbol)
        new_image.append(new_row)

    if are_all_lit and algorithm[511] == '.':
        are_all_lit = False
    elif not are_all_lit and algorithm[0] == '#':
        are_all_lit = True

    return new_image

def get_surrounding_squares_in_binary(image, row, col):
    global are_all_lit
    squares = ''
    for r_diff in [-1, 0 , 1]:
        for c_diff in [-1, 0, 1]:
            squares += get_bin_from_place(image, row + r_diff, col + c_diff)
    return squares
    
def get_bin_from_place(image, row, col):
    global are_all_lit
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
        return '0' if not are_all_lit else '1'
    sym = image[row][col]
    return '1' if sym == '#' else '0'

def count_lights_in_image(image):
    count = 0
    for row in image:
        for el in row:
            if el == '#':
                count += 1
    return count
