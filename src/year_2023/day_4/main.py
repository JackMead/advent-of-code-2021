from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2023/day_4/input.txt')
    sum = 0
    for line in input:
        sum += score_card(line)
    print(f"Day 4 Q1: {sum}")

    total_scratchcards = count_total_scratchcards(input)
    print(f"Day 4 Q2: {total_scratchcards}")

def score_card(input):
    matches = count_winners(input)
    return 2**(matches-1) if matches > 0 else 0

def count_total_scratchcards(input):
    scratchcards = {}

    for i in range(1, len(input) + 1):
        scratchcards[i] = 1

    for i in range(1, len(input) + 1):
        line = input[i - 1]
        num_winners = count_winners(line)
        for j in range(1, num_winners + 1):
            scratchcards[i + j] += scratchcards[i]
    
    # print(scratchcards)
    return sum(scratchcards.values())

def count_winners(line):
    number_sets = line.split('|')
    winners = list(filter(None, number_sets[0].split(' ')[2:]))
    choices = list(filter(None, number_sets[1].split(' ')))

    matches = len([1 for choice in choices if choice in winners])
    return matches
