from src.helpers.files import load_txt_file_list_of_nums

def run():
    nums = load_txt_file_list_of_nums("./src/day_1/input.txt")
    print(f"Day 1 Q1: There are {count_number_of_increases(nums)} increases")
    print(f"Day 2 Q2: There are {count_number_of_increases_with_sliding_window(nums)} increases")
    
def count_number_of_increases(nums):
    previous = None
    count = 0
    for i in range(len(nums)):
        new = nums[i]
        if previous and new > previous:
            count += 1
        previous = new
    return count

def count_number_of_increases_with_sliding_window(nums):
    window_size = 3
    window = [None] * window_size
    count = 0
    # assume window smaller than length of nums

    window = nums[:window_size]
    for i in range(3, len(nums)):
        previous = nums[i-3]
        new = nums[i]
        if new > previous:
            count += 1
    return count