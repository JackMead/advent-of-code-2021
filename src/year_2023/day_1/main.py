from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2023/day_1/input.txt')

    sum = part_one(input)
    print(f"Day 1 Q1: {sum}")

    sum = part_two(input)
    print(f"Day 1 Q2: {sum}")

def part_one(input):
    sum = 0
    for line in input:
        sum += get_numbers_from_first_and_last_digits(line)
    return sum

def part_two(input):
    sum = 0
    for line in input:
        sum += get_numbers_from_first_and_last_digits_inc_words(line)
    return sum


def get_numbers_from_first_and_last_digits(string):
    first = 0
    last = 0
    for char in string:
        if char.isdigit():
            first = int(char)
            break
    for char in string[::-1]:
        if char.isdigit():
            last = int(char)
            break
    return first * 10 + last

numbers_as_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words_to_numbers = {
    "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9
}

def get_numbers_from_first_and_last_digits_inc_words(string):
    first = 0
    last = 0
    for index in range(len(string)):
        char = string[index]
        if char.isdigit():
            first = int(char)
            break
        word_value = get_word(index, string)
        # print(word_value)
        if word_value:
            first = word_value
            # print("Hit")
            # print(word_value)
            break

    for index in range(len(string) - 1, -1, -1):
        char = string[index]
        if char.isdigit():
            last = int(char)
            break
        word_value = get_word_backwards(index, string)
        # print(word_value)
        if word_value:
            last = word_value
            # print("Hit")
            # print(word_value)
            break

    return first * 10 + last

def get_word(index, string):
    first = None
    char = string[index]
    matching_words = [word for word in numbers_as_words if word[0] == char]
    # print(matching_words)
    for word in matching_words:
        # print(index + len(word))
        # print(string[index: index + len(word)])
        if index + len(word) <= len(string) and string[index: index + len(word)] == word:
            first = words_to_numbers[word]
            break
    return first

def get_word_backwards(index, string):
    last = None
    char = string[index]
    matching_words = [word for word in numbers_as_words if word[-1] == char]
    # print(matching_words)
    for word in matching_words:
        # print(index + len(word))
        # print(string[index: index + len(word)])
        if index - len(word) >= -1 and string[index - len(word) + 1: index + 1] == word:
            last = words_to_numbers[word]
            break
    return last
