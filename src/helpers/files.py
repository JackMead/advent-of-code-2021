from typing import List

def load_txt_file(path) -> List[str]:
    with open(path) as txtFile:
        return txtFile.read().splitlines()

def load_txt_file_list_of_nums(path) -> List[int]:
    return [int(line) for line in load_txt_file(path)]