from src.helpers.files import load_txt_file

def run():
    binary_strings = load_txt_file("./src/day_3/input.txt")
    gamma, epsilon = get_gamma_and_epsilon(binary_strings)
    print(f"Day 3 Q1: product = {gamma * epsilon}")

    o2, co2 = get_o2_and_co2(binary_strings)
    print(f"Day 3 Q2: product = {o2 * co2}")

def get_gamma_and_epsilon(inputs):
    input_length = len(inputs[0])
    num_inputs = len(inputs)
    count = [0] * input_length
    for input in inputs:
        for index in range(input_length):
            if input[index] == '1':
                count[index] += 1
    
    gamma_array = ['1' if count[index] > num_inputs / 2 else '0' for index in range(input_length)]
    epsilon_array = ['1' if count[index] < num_inputs / 2 else '0' for index in range(input_length)]

    gamma = int("".join(gamma_array), 2)
    epsilon = int("".join(epsilon_array), 2)

    return gamma, epsilon

def get_o2_and_co2(inputs):

    return get_o2(inputs), get_co2(inputs)

def get_o2(inputs):
    remaining_values = inputs.copy()
    input_length = len(inputs[0])
    
    for i in range(input_length):
        count = sum([1 if input[i] == '1' else 0 for input in remaining_values])
        if count >= (len(remaining_values) / 2):
            remaining_values = [value for value in remaining_values if value[i] == '1' ]
        else:
            remaining_values = [value for value in remaining_values if value[i] == '0' ]
        if len(remaining_values) == 1:
            return int(remaining_values[0],2)

    print(f"Shouldn't get here")
    print(remaining_values)
    return 0

def get_co2(inputs):
    remaining_values = inputs.copy()
    input_length = len(inputs[0])
    
    for i in range(input_length):
        count = sum([1 if input[i] == '1' else 0 for input in remaining_values])
        if count >= (len(remaining_values) / 2):
            remaining_values = [value for value in remaining_values if value[i] == '0' ]
        else:
            remaining_values = [value for value in remaining_values if value[i] == '1' ]
        if len(remaining_values) == 1:
            return int(remaining_values[0],2)

    print(f"Shouldn't get here")
    print(remaining_values)
    return 0