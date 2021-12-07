from src.helpers.files import load_txt_file

def run():
    input = load_txt_file("./src/day_4/input.txt")
    score = get_winning_score(input)
    print(f"Day 4 Q1: Winning score = {score}")

def get_winning_score(input):
    return 0