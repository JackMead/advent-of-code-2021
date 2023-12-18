from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2021/day_10/input.txt')
    score = score_corrupted_lines(input)
    print(f"Day 10 Q1: Total corrupted score = {score}")
    score = score_incomplete_lines(input)
    print(f"Day 10 Q2: Total incomplete score = {score}")

def score_corrupted_lines(input):
    corrupted_chars = [get_corrupted_char(line) for line in input]
    score = [score_char(char) for char in corrupted_chars]
    return sum(score)

def score_incomplete_lines(input):
    missing_braces = [get_missing_braces(line) for line in input]
    scores = [score_missing_braces(missing) for missing in missing_braces]
    filtered_scores = [score for score in scores if score > 0]
    return middle_score(filtered_scores)

def get_missing_braces(line):
    left_hand_brace = ['(', '[', '{', '<']
    right_hand_brace = [')', ']', '}', '>']

    stack = []
    # find current status, and whether corrupt
    for char in line:
        if char in left_hand_brace:
            stack.append(char)
            continue
        if char in right_hand_brace:
            if len(stack) == 0 or not braces_match(stack[-1], char):
                return ''
            stack.pop()
            continue
        raise Exception(f"char not recognised: {char}")
    
    missing = []
    stack.reverse()
    for char in stack:
        index_in_left = left_hand_brace.index(char)
        corresponding_brace = right_hand_brace[index_in_left]
        missing.append(corresponding_brace)
    return missing

def score_missing_braces(missing_line):
    running_total = 0
    brace_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    for char in missing_line:
        running_total *= 5
        running_total += brace_scores[char]
    return running_total

def middle_score(scores):
    length = len(scores)
    middle_index = (length - 1) // 2
    return sorted(scores)[middle_index]

def get_corrupted_char(line):
    left_hand_brace = ['(', '[', '{', '<']
    right_hand_brace = [')', ']', '}', '>']

    stack = []
    for char in line:
        if char in left_hand_brace:
            stack.append(char)
            continue
        if char in right_hand_brace:
            if len(stack) == 0 or not braces_match(stack[-1], char):
                return char
            stack.pop()
            continue
        raise Exception(f"char not recognised: {char}")

def braces_match(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True
    if left == '<' and right == '>':
        return True
    return False

def score_char(char):
    if char == None:
        return 0
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return scores[char]