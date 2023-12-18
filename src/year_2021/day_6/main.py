from src.helpers.files import load_txt_file

EMPTY_TIMER = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }

def run():
    input = load_txt_file('./src/year_2021/day_6/input.txt')
    count = count_lantern_fish_after_days(input[0], 80)
    print(f"Day 6 Q1: {count}")
    count = count_lantern_fish_after_days(input[0], 256)
    print(f"Day 6 Q2: {count}")

def count_lantern_fish_after_days(inputs, days):
    timer_counts = convert_input_to_dictionary(inputs)
    for i in range(days):
        timer_counts = update_timers(timer_counts)
    total_count = get_total_count_from_timers(timer_counts)
    return total_count

def get_total_count_from_timers(timer_counts):
    return sum(timer_counts.values())

def update_timers(timer_counts):
    new_dict = EMPTY_TIMER.copy()
    for i in range(1, 9):
        new_dict[i-1] = timer_counts[i]
    new_dict[6] += timer_counts[0]
    new_dict[8] = timer_counts[0]
    return new_dict

def convert_input_to_dictionary(inputs):
    timer_counts = EMPTY_TIMER.copy()
    timers = [int(num) for num in inputs.split(',')]
    for timer in timers:
        timer_counts[timer] = timer_counts[timer] + 1
    return timer_counts