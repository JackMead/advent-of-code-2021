from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2023/day_2/input.txt')
    games = parse_games(input)

    sum = 0
    for game in games:
        if is_possible(game):
            print(f"{game['id']} is possible")
            sum += game['id']
        else:
            print(f"{game['id']} aint possible!")
            print(game['draws'])

    print(f"Day 2 Q1: {sum}")

    sum = 0
    for game in games:
        sum += power_of_game(game)
    print(f"Day 2 Q2: {sum}")

def power_of_game(game):
    min_red_required = max(draw['red'] for draw in game['draws'])
    min_green_required = max(draw['green'] for draw in game['draws'])
    min_blue_required = max(draw['blue'] for draw in game['draws'])
    return min_red_required * min_green_required * min_blue_required

def parse_games(input):
    return [
        {
            'id': i + 1,
            'draws': get_draws(input[i])
        }
        for i in range(len(input))
    ]

def get_draws(line):
    draws = line.split(': ')[1]
    sections = draws.split(';')
    all = []
    for section in sections[0:]:
        result = {
            'red': 0,
            'blue': 0,
            'green': 0
        }
        colours = section.split(',')
        for colour in colours:
            if 'green' in colour:
                result['green'] = int(colour[0:-6])
            elif 'red' in colour:
                result['red'] = int (colour[0:-4])
            elif 'blue' in colour:
                result['blue'] = int (colour[0:-5])
                
        all.append(result)
    return all

def is_possible(game):
    return all(
        draw['red'] <= 12 and draw['green'] <= 13 and draw['blue'] <= 14
        for draw in game['draws']
    )