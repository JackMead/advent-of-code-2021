from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/year_2023/day_5/input.txt')
    info = parse_input(input)
    location = find_nearest_valid_location(info)

    print(f"Day 5 Q1: {location}")
    
    location = find_nearest_valid_location(info, part_two = True)
    print(f"Day 5 Q2: {location}")

def parse_input(input):
    info = Info(input)
    return info

def find_nearest_valid_location(info, part_two = False):
    lowest = None
    if not part_two:
        for seed in info.seeds:
            location = info.get_location_for_seed(seed)
            # print(f"Seed {seed} has location {location}")
            if not lowest or location < lowest:
                lowest = location
        return lowest

    print("Here")
    ranges_to_check = []
    # experimentally reasonably quick - too big slows the next bit
    # too small slows the specific checks
    step_size = 5000
    # if part_two:
    for index in range(0, len(info.seeds)):
        if index % 2 == 0:
            start_range = info.seeds[index]
            location = info.get_location_for_seed(start_range)
            if not lowest or location < lowest:
                lowest = location
        else:
            num = info.seeds[index]
            local_step_size = min(num - 1, step_size)
            for seed in range(start_range, start_range + num, local_step_size):
                location = info.get_location_for_seed(seed)
                # print(f"Checks: Seed {seed} has location {location}")
                if location < lowest:
                    lowest = location
                    print(f"adding new range: {seed - local_step_size}, {seed}")
                    ranges_to_check.append([seed - local_step_size, seed])
    
    # return
    for segment in ranges_to_check:
        for seed in range(segment[0], segment[1]):
            location = info.get_location_for_seed(seed)
            print(f"Seed {seed} has location {location}")
            if not lowest or location < lowest:
                lowest = location
    return lowest


class Info:
    def __init__(self, input):
        self.seeds = self.get_seeds(input)
        self.seed_to_soil = self.get_map(1, input)
        self.soil_to_fertilizer = self.get_map(2, input)
        self.fertilizer_to_water = self.get_map(3, input)
        self.water_to_light = self.get_map(4, input)
        self.light_to_temp = self.get_map(5, input)
        self.temp_to_humidity = self.get_map(6, input)
        self.humidity_to_location = self.get_map(7, input)

    def get_seeds(self, input):
        return [int(val) for val in input[0][7:].split(' ')]

    def get_map(self, num, input):
        n = 0
        map = Map()
        for line in input:
            if line == '':
                n += 1
                continue
            if n > num:
                break
            if n == num:
                if line[0].isnumeric():
                    split = line.split(' ')
                    source_start = int(split[1])
                    length = int(split[2])
                    dest_start = int(split[0])
                    map.add_range(source_start, dest_start, length)
        return map
    
    def get_location_for_seed(self, seed):
        soil = self.seed_to_soil.get(seed)
        fert = self.soil_to_fertilizer.get(soil)
        water = self.fertilizer_to_water.get(fert)
        light = self.water_to_light.get(water)
        temp = self.light_to_temp.get(light)
        humidity = self.temp_to_humidity.get(temp)
        location = self.humidity_to_location.get(humidity)
        return location
    
class Map():

    def __init__(self):
        self.range = []

    def add_range(self, source_start, dest_start, length):
        self.range.append([source_start, dest_start, length])

    def get(self, value):
        for section in self.range:
            start = section[0]
            if value >= start and value < start + section[2]:
                return section[1] + (value - section[0])
        return value