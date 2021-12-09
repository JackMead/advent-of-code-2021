from typing import List

def load_txt_file(path) -> List[str]:
    with open(path) as txtFile:
        return txtFile.read().splitlines()

def load_txt_file_list_of_nums(path) -> List[int]:
    return [int(line) for line in load_txt_file(path)]

def load_list_of_nums_on_line_1(path) -> List[int]:
    return [int(num) for num in load_first_line(path).split(',')]

def load_first_line(path) -> str:
    return load_txt_file(path)[0]