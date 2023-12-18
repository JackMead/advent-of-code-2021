from src.helpers.files import load_list_of_nums_on_line_1

def run():
    inputs = load_list_of_nums_on_line_1('./src/year_2021/day_7/input.txt')
    cost = get_minimal_alignment_cost(inputs)
    print(f"Day 7 Q1: minimal cost {cost}")
    cost = get_actual_minimal_alignment_cost(inputs)
    print(f"Day 7 Q2: minimal cost with actual engineering = {cost}")

def get_minimal_alignment_cost(inputs):
    # lazy first pass - just check all?
    # better approach, bring number furthest from average towards it, then iterate?
    # stick with lazy for now

    smallest = min(inputs)
    biggest = max(inputs)

    best_cost = None
    for i in range(smallest, biggest + 1):
        fuel_cost = sum([abs(num - i) for num in inputs])
        if best_cost == None or fuel_cost < best_cost:
            best_cost = fuel_cost

    return best_cost

def get_actual_minimal_alignment_cost(inputs):
    smallest = min(inputs)
    biggest = max(inputs)

    best_cost = None
    for i in range(smallest, biggest + 1):
        fuel_cost = sum([get_cost_of_steps(abs(num - i)) for num in inputs])
        if best_cost == None or fuel_cost < best_cost:
            best_cost = fuel_cost

    return best_cost

# costs according to triangular numbers
def get_cost_of_steps(number):
    return (number * (number + 1)) // 2
