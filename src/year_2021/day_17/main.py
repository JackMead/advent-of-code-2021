from src.helpers.files import load_txt_file

RESULT_OVER='OVER'
RESULT_IN='IN'
RESULT_UNDER='BELOW'
RESULT_THROUGH='THROUGH'

def run():
    input = load_txt_file('./src/year_2021/day_17/input.txt')
    max_y = find_max_y_position_reaching_target(input[0])
    print(f"Day 17 Q1: Max Y hit: {max_y}")
    count = count_distinct_velocities(input[0])
    print(f"Day 17 Q2: Count: {count}")

'''
Assumes target is to the right, i.e. positive
'''
def count_distinct_velocities(input):
    target = read_input(input)
    min_x_speed, max_x_speed = find_x_speed_range(target)
    solutions = find_all_solutions(target, min_x_speed, max_x_speed)
    return solutions

def find_max_y_position_reaching_target(input):
    target = read_input(input)
    min_x_speed, max_x_speed = find_x_speed_range(target)
    max_y_position = find_best_solution(target, min_x_speed, max_x_speed)
    return max_y_position

def find_x_speed_range(target):
    target_horizontal_distance = target.min_x
    count = 0
    while target_horizontal_distance > 0:
        count += 1
        target_horizontal_distance -= count
    min_x_speed = count
    max_x_speed = target.max_x
    return min_x_speed, max_x_speed

def find_all_solutions(target, min_vx, max_vx):
    count = 0
    for x_speed in range(min_vx, max_vx + 1):
        count += count_solutions_for_x_speed(target, x_speed)
    return count

def find_best_solution(target, min_x_speed, max_x_speed):
    # start from slowest speed, and try find if we can hit
    best_y = None
    for x_speed in range(min_x_speed, max_x_speed + 1):
        best_y_for_speed = find_best_y_for_x_speed(target, x_speed)
        if has_improved(best_y, best_y_for_speed):
            print(f"New best: {best_y_for_speed} from vx {x_speed}")
            best_y = best_y_for_speed
    return best_y

def count_solutions_for_x_speed(target, x_speed):
    count = 0
    max_y_speed = 1000
    for y_speed in range(target.min_y, max_y_speed + 1):
        result, best_y_from_shot = shoot(target, x_speed, y_speed)
        if result == RESULT_IN:
            count += 1
    return count

def find_best_y_for_x_speed(target, x_speed):
    y_speed = 0
    best_y = None

    # total guess, need to work out how to estimate this
    max_y_speed = 1000
    for y_speed in range(target.min_y, max_y_speed + 1):
        result, best_y_from_shot = shoot(target, x_speed, y_speed)
        if result == RESULT_IN and has_improved(best_y, best_y_from_shot):
            best_y = best_y_from_shot

    return best_y

def has_improved(orig, new):
    return not orig or (new and new > orig)

def shoot(target, x_speed, y_speed):
    debug = (x_speed == 6 and y_speed == 9)
    x_position = 0
    y_position = 0
    positions = []
    while unfinished(target, x_position, y_position):
        x_position += x_speed
        y_position += y_speed
        if x_speed > 0:
            x_speed -= 1
        y_speed -= 1
        positions.append((x_position, y_position))

    result = get_result(target, x_position, y_position)
    if debug:
        print(positions)
        print(result)
    y_coords = [pos[1] for pos in positions]
    return result, max(y_coords)

def unfinished(target, x_position, y_position):
    return get_result(target, x_position, y_position) == None

def get_result(target, x, y):
    if x >= target.min_x and x <= target.max_x and y >= target.min_y and y <= target.max_y:
        return RESULT_IN
    if y < target.min_y and x < target.min_x:
        return RESULT_UNDER
    if x > target.max_x and y > target.max_y:
        return RESULT_OVER
    if x > target.max_x or y < target.min_y:
        return RESULT_THROUGH
    return None

class Target():
    def __init__(self, string):
        string_without_padding = string[15:]
        x, y = string_without_padding.split()
        # remove more padding
        x = x[:-1]
        y = y[2:]
        self.min_x, self.max_x = (int(num) for num in x.split('..'))
        self.min_y, self.max_y = (int(num) for num in y.split('..'))

def read_input(input):
    return Target(input)