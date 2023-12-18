from src.helpers.files import load_txt_file
import json
import math
import copy

def run():
    input = load_txt_file('./src/year_2021/day_18/input.txt')
    magnitude = get_magnitude_of_sum(input)
    print(f"Day 18 Q1: magnitude = {magnitude}")
    max_mag = get_max_magnitude_of_sum(input)
    print(f"Day 18 Q2: max mag of sum = {max_mag}")

def get_max_magnitude_of_sum(input):
    nums = parse_inputs(input)

    max_mag = None
    for a in nums:
        for b in nums:
            if a == b:
                continue
            total = add_nums(a, b)
            mag = get_magnitude(total)
            if not max_mag or mag > max_mag:
                max_mag = mag
    return max_mag

def get_magnitude_of_sum(input):
    array_of_nums = parse_inputs(input)
    running_total = array_of_nums[0]
    for i in range(1, len(array_of_nums)):
        running_total = add_nums(running_total, array_of_nums[i])
    magnitude = get_magnitude(running_total)
    return magnitude

def get_magnitude(total):
    if (isinstance(total, int)):
        return total
    return 3 * get_magnitude(total[0]) + 2 * get_magnitude(total[1])

def add_nums(n1, n2):
    n1c = copy.deepcopy(n1)
    n2c = copy.deepcopy(n2)
    naive_sum = add_naively(n1c, n2c)
    reduced_sum = reduce_num(naive_sum)
    return reduced_sum

def reduce_num(num):
    while True:
        exploded = explode_if_necessary(num)
        if exploded:
            continue
        splitted = split_if_necessary(num)
        if splitted:
            continue
        break
    return num

def explode_if_necessary(num):
    for idx1, l1  in enumerate(num):
        if isinstance(l1, list):
            for idx2, l2 in enumerate(l1):
                if isinstance(l2, list):
                    for idx3, l3 in enumerate(l2):
                        if isinstance(l3, list):
                            for idx4, l4 in enumerate(l3):
                                if isinstance(l4, list):
                                    if idx4 > 0:
                                        add_to_last_num_before(l3, idx4, l4[0])
                                    elif idx3 > 0:
                                        add_to_last_num_before(l2, idx3, l4[0])
                                    elif idx2 > 0:
                                        add_to_last_num_before(l1, idx2, l4[0])
                                    elif idx1 > 0:
                                        add_to_last_num_before(num, idx1, l4[0])

                                    if idx4 < len(l3) -1:
                                        add_to_next_num_from(l3, idx4, l4[1])
                                    elif idx3 < len(l2) - 1:
                                        add_to_next_num_from(l2, idx3, l4[1])
                                    elif idx2 < len(l1) - 1:
                                        add_to_next_num_from(l1, idx2, l4[1])
                                    elif idx1 < len(num) - 1:
                                        add_to_next_num_from(num, idx1, l4[1])

                                    l3[idx4] = 0
                                    return True
    return False

def add_to_last_num_before(arr, idx, value):
    for inner_index in range(idx -1 , -1, -1):
        el = arr[inner_index]
        if isinstance(el, int):
            arr[inner_index] += value
            return
        if isinstance(el, list):
            add_to_last_num_before(el, len(el), value)
            return

def add_to_next_num_from(arr, idx, value):
    for inner_index in range(idx + 1, len(arr)):
        el = arr[inner_index]
        if isinstance(el, int):
            arr[inner_index] += value
            return
        if isinstance(el, list):
            add_to_next_num_from(el, -1, value)
            return

def split_if_necessary(arr):
    for inner_index in range(0, len(arr)):
        el = arr[inner_index]
        if isinstance(el, int):
            if el > 9:
                arr[inner_index] = [el // 2, math.ceil(el / 2)]
                return True
        if isinstance(el, list):
            splitted = split_if_necessary(el)
            if splitted:
                return True
    return False

def add_naively(n1, n2):
    new = [n1, n2]
    return new

def parse_inputs(input):
    nums = []
    for line in input:
        nums.append(json.loads(line))
    return nums