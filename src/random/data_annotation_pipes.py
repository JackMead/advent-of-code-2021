from typing import Any, List

# '═', '║', '╔', '╗', '╚', '╝', '╠', '╣', '╦', '╩'

valid_left = ['═', '╚', '╔', '╠', '╦', '╩']
valid_right = ['═', '╗', '╝', '╣', '╦', '╩']
valid_up = ['║', '╔', '╗', '╠', '╣', '╦']
valid_down = ['║', '╚', '╝', '╠', '╣', '╩']
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def load_input(file) -> List[List[Any]]:
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
        split_lines = [
            line.split() for line in lines
        ]
        typed_lines = [
            [l[0], int(l[1]), int(l[2])] for l in split_lines
        ]

    return typed_lines

def find_sinks(input: List[List[Any]]) -> str:
    map_dict = {}
    for l in input:
        map_dict[(l[1], l[2])] = l[0]

    source_entry = next(l for l in input if l[0] == '*')
    start_position = (source_entry[1], source_entry[2])

    done = set()
    found_sinks = []

    def dfs(pos_to_check):
        if pos_to_check in done:
            return
        done.add(pos_to_check)
        
        to_check = []
        current = map_dict[pos_to_check]
        if current == '*' or current in valid_right:
            left = (pos_to_check[0] - 1, pos_to_check[1])
            to_check.append((left, valid_left))
        if current == '*' or current in valid_left:
            right = (pos_to_check[0] + 1, pos_to_check[1])
            to_check.append((right, valid_right))
        if current == '*' or current in valid_up:
            down = (pos_to_check[0], pos_to_check[1] - 1)
            to_check.append((down, valid_down))
        if current == '*' or current in valid_down:
            up = (pos_to_check[0], pos_to_check[1] + 1)
            to_check.append((up, valid_up))
        for pos, valid in to_check:
            if pos[0] < 0 or pos[1] < 0:
                continue
            if pos not in map_dict:
                continue
            if map_dict[pos] in valid and pos not in done:
                
                print(f"{pos} is valid for liquid from {pos_to_check}")
                dfs(pos)
            if map_dict[pos] in letters:
                done.add(pos)
                print(f"{pos} has sink")
                found_sinks.append(map_dict[pos])

    dfs(start_position)

    found_sinks.sort()
    return ''.join(found_sinks)
