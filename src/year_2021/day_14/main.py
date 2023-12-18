from src.helpers.files import load_txt_file
from collections import Counter

def run():
    input = load_txt_file('./src/year_2021/day_14/input.txt')
    range_of_scores = get_range_of_element_counts_at_step_X(input, 10)
    print(f"Day 14 Q1: range = {range_of_scores}")
    range_of_scores = get_range_of_element_counts_at_step_X_efficient(input, 40)
    print(f"Day 14 Q2: range = {range_of_scores}")

def get_range_of_element_counts_at_step_X(input, step_count):
    polymer, rules = read_input(input)
    for i in range(step_count):
        polymer = apply_rules_to_polymer(polymer, rules)
    counts = count_occurences(polymer)
    range_of_scores = get_range_of_occurences(counts)
    return range_of_scores

def get_range_of_element_counts_at_step_X_efficient(input, step_count):
    polymer, rules = read_input(input)
    pairs = build_pairs(polymer)
    for i in range(step_count):
        pairs = apply_rules_to_polymer_efficient(pairs, rules)
    counts = count_occurences_from_dict(pairs, polymer)
    range_of_scores = get_range_of_occurences(counts)
    return range_of_scores

def apply_rules_to_polymer(polymer, rules):
    new_polymer = [polymer[0]]
    for i in range(1, len(polymer)):
        pair = polymer[i-1] + polymer[i]
        insertion = rules[pair]
        new_polymer.append(insertion)
        new_polymer.append(polymer[i])
    return new_polymer

def apply_rules_to_polymer_efficient(pairs, rules):
    new_pairs = pairs.copy()
    for pair in pairs.keys():
        insertion = rules[pair]
        first_new_pair = pair[0] + insertion
        second_new_pair = insertion + pair[1]
        if first_new_pair not in new_pairs:
            new_pairs[first_new_pair] = 0
        if second_new_pair not in new_pairs:
            new_pairs[second_new_pair] = 0
        new_pairs[first_new_pair] += pairs[pair]
        new_pairs[second_new_pair] += pairs[pair]
        new_pairs[pair] -= pairs[pair]
    return new_pairs

def build_pairs(polymer):
    pairs = {}
    for i in range(1, len(polymer)):
        pair = polymer[i-1] + polymer[i]
        if pair not in pairs:
            pairs[pair] = 0
        pairs[pair] += 1
    return pairs

class Rule():
    def __init__(self, pair, insert):
        self.pair = pair
        self.insert = insert

def read_input(input):
    polymer = input[0]
    rules = {rule[0]:rule[1] for rule in (line.split(' -> ') for line in input[2:])}
    return polymer, rules

def count_occurences(polymer):
    return dict(Counter(polymer))

def count_occurences_from_dict(polymer_dict, original_polymer):
    element_dict = {}
    for pair, value in polymer_dict.items():
        if pair[0] not in element_dict:
            element_dict[pair[0]] = 0
        element_dict[pair[0]] += value
        if pair[1] not in element_dict:
            element_dict[pair[1]] = 0
        element_dict[pair[1]] += value
    for key in element_dict.keys():
        element_dict[key] = element_dict[key] // 2
    element_dict[original_polymer[0]] += 1
    element_dict[original_polymer[-1]] += 1
    return element_dict

def get_range_of_occurences(counter):
    return max(counter.values()) - min(counter.values())
