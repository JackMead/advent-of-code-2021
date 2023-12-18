from src.helpers.files import load_txt_file
from abc import ABC, abstractmethod

def run():
    input = load_txt_file('./src/year_2021/day_21/input.txt')
    die = DeterministicDie(100)
    points = get_loser_points(input, die)
    print(f"Day 21 Q1: loser scores {points}")
    winners = get_winning_universes(input)
    print(f"Day 21 Q2: winner wins in {winners} universes")

class Die(ABC):
    @abstractmethod
    def roll(self):
        pass

class DeterministicDie(Die):

    def __init__(self, max):
        self.max = max
        self.current = 1

    def roll(self):
        current = self.current
        self.current += 1
        if self.current > self.max:
            self.current - self.max
        return current

class Player():
    final_square = 10
    def __init__(self, position):
        self.position = position
        self.points = 0

    def advance(self, num):
        self.position += num
        while self.position > Player.final_square:
            self.position -= Player.final_square
        self.points += self.position

    def has_won(self):
        return self.points >= 1000

MAX_SCORE = 21

def get_winning_universes(input):
    p1, p2 = get_players(input)
    all_scores = build_initial_scores()
    all_scores[(0, 0, p1.position, p2.position, True)] = 1
    while (some_game_incomplete(all_scores)):
        for k,v in all_scores.items():
            if v > 0 and k[0] < MAX_SCORE and k[1] < MAX_SCORE:
                next_rolls(all_scores, k, v)
                all_scores[k] = 0
    return count_winning_score(all_scores)

def build_initial_scores():
    all_scores = {}
    for p1_score in range(31):
        for p2_score in range(31):
            for p1_pos in range(1, 11):
                for p2_pos in range(1, 11):
                    for p1_turn in [True, False]:
                        all_scores[(p1_score, p2_score, p1_pos, p2_pos, p1_turn)] = 0
    return all_scores

def next_rolls(all_scores, k, v):
    for rolls in possible_dirac_rolls:
        player_pos = k[2] if k[4] else k[3]
        player_score = k[0] if k[4] else k[1]
        total = sum(rolls)
        
        player_pos += total
        while player_pos > Player.final_square:
            player_pos -= Player.final_square
        player_score += player_pos
        p1_pos = player_pos if k[4] else k[2]
        p2_pos = k[3] if k[4] else player_pos
        p1_score = player_score if k[4] else k[0]
        p2_score = k[1] if k[4] else player_score
        all_scores[(p1_score, p2_score, p1_pos, p2_pos, not k[4])] += v

def count_winning_score(all_scores):
    p1 = 0
    p2 = 0
    for k,v in all_scores.items():
        if k[0] >= MAX_SCORE:
            p1 += v
        elif k[1] >= MAX_SCORE:
            p2 += v
    return max(p1, p2)

possible_dirac_rolls = []
for i in [1,2,3]:
    for j in [1,2,3]:
        for k in [1,2,3]:
            possible_dirac_rolls.append([i,j,k])

def some_game_incomplete(all_scores):
    for k,v in all_scores.items():
        if v > 0 and k[0] < 21 and k[1] < 21:
            return True
    return False

def get_loser_points(input, die):
    p1, p2 = get_players(input)
    count = 0
    while(True):
        rolls = [die.roll(), die.roll(), die.roll()]
        total = sum(rolls)
        p1.advance(total)
        count += 3
        if p1.has_won():
            return count * p2.points
        rolls = [die.roll(), die.roll(), die.roll()]
        total = sum(rolls)
        p2.advance(total)
        count += 3
        if p2.has_won():
            return count * p1.points
            
    raise Exception("Broke!")

def get_players(input):
    p1_start = int(input[0].split()[-1])
    p2_start = int(input[1].split()[-1])
    return Player(p1_start), Player(p2_start)