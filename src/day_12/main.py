from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/day_12/input.txt')
    count = count_paths_through_caves(input)
    print(f"Day 12 Q1: There are {count} paths")
    count = count_paths_through_caves_allowing_repeat(input)
    print(f"Day 12 Q2: There are {count} paths with a repeat")

def count_paths_through_caves(input):
    nodes = get_nodes(input)
    paths = find_all_paths_without_waste(nodes)
    return len(paths)

def count_paths_through_caves_allowing_repeat(input):
    nodes = get_nodes(input)
    paths = find_all_paths_with_some_waste(nodes)
    return len(paths)

def get_nodes(input):
    nodes = {}
    for line in input:
        sides = line.split('-')
        add_path(nodes, sides[0], sides[1])
    return nodes

def add_path(nodes, a, b):
    if a not in nodes:
        nodes[a] = []
    if b not in nodes:
        nodes[b] = []
    nodes[a].append(b)
    nodes[b].append(a)

def find_all_paths_without_waste(nodes):
    paths = [['start']]
    finished = []
    while len(paths) > 0:
        path = paths.pop(0)
        if path[-1] == 'end':
            continue
        for possible in nodes[path[-1]]:
            if is_valid(path, possible):
                new_path = path.copy()
                new_path.append(possible)
                if possible == 'end':
                    finished.append(new_path)
                else:
                    paths.append(new_path)
    return finished

def find_all_paths_with_some_waste(nodes):
    paths = [['start']]
    finished = []
    while len(paths) > 0:
        path = paths.pop(0)
        if path[-1] == 'end':
            continue
        for possible in nodes[path[-1]]:
            if is_valid_with_waste(path, possible):
                new_path = path.copy()
                new_path.append(possible)
                if possible == 'end':
                    finished.append(new_path)
                else:
                    paths.append(new_path)
    return finished

def is_valid(path, possible):
    return possible.isupper() or possible not in path

def is_valid_with_waste(path, possible):
    return possible.isupper() or (possible not in path) or (possible != 'start' and no_repeats_yet(path))

def no_repeats_yet(path):
    small_caves = [cave for cave in path if cave.islower()]
    return len(small_caves) == len(set(small_caves))
    