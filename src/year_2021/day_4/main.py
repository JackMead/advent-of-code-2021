from src.helpers.files import load_txt_file

HIT = '*'

def run():
    input = load_txt_file("./src/year_2021/day_4/input.txt")
    score = get_winning_score(input)
    print(f"Day 4 Q1: Winning score = {score}")
    score = get_losing_score(input)
    print(f"Day 4 Q2: Losing score = {score}")

def get_winning_score(input):
    numbers = get_numbers(input)
    boards = get_boards(input)
    index = 0
    while(no_board_finished(boards)):
        mark_number(boards, numbers[index])
        index += 1
    
    for board in boards:
        if is_board_finished(board):
            return score_board(board) * numbers[index - 1]

    raise Exception("No board won")

def get_losing_score(input):
    numbers = get_numbers(input)
    boards = get_boards(input)
    index = 0
    while(some_board_unfinished(boards)):
        for board in boards:
            if is_board_finished(board):
                boards.remove(board)
        mark_number(boards, numbers[index])
        index += 1
    
    for board in boards:
        if is_board_finished(board):
            return score_board(board) * numbers[index - 1]

    raise Exception("No board won")

def some_board_unfinished(boards):
    unfinished = [not is_board_finished(board) for board in boards]
    return any(unfinished)

def mark_number(boards, number):
    for board in boards:
        for row in board:
            for index in range(len(row)):
                if row[index] == number:
                    row[index] = HIT

def score_board(board):
    score = 0
    for row in board:
        for element in row:
            if element != HIT:
                score += element
    return score

def get_numbers(input):
    return [int(num) for num in input[0].split(',')]

def get_boards(input):
    boards = []
    board = None
    for row in input[1:]:
        if row.strip() == '':
            if board != None:
                boards.append(board)
            board = []
        else:
            board.append([int(num) for num in row.split()])
    if input[-1].strip() != '':
        boards.append(board)
    return boards

def no_board_finished(boards):
    unfinished = [not is_board_finished(board) for board in boards]
    return all(unfinished)

def is_board_finished(board):
    for row in board:
        if row == [HIT] * len(row):
            return True

    for i in range(len(board[0])):
        all_hit = True
        for row in board:
            if row[i] != HIT:
                all_hit = False
                break
        if all_hit:
            return True
    return False