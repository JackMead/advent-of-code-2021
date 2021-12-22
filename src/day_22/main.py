from src.helpers.files import load_txt_file

def run():
    input = load_txt_file('./src/day_22/input.txt')
    count = count_active_in_initialisation_region(input)
    print(f"Day 22 Q1: {count} cubes are on in initialisation region")
    count = count_active_everywhere(input)
    print(f"Day 22 Q2: {count} cubes are on across reactor")

# try brute force first
def count_active_in_initialisation_region(input):
    instructions = parse_input(input)
    on_lights = set()
    for instruction in instructions:
        if not instruction.is_valid():
            continue
        for x in range(instruction.x_min, instruction.x_max + 1):
            for y in range(instruction.y_min, instruction.y_max + 1):
                for z in range(instruction.z_min, instruction.z_max + 1):
                    coord = (x,y,z)
                    if instruction.toggle == 'on':
                        on_lights.add(coord)
                    elif instruction.toggle == 'off' and coord in on_lights:
                        on_lights.remove(coord)
    return len(on_lights)

def count_active_everywhere_brute(input):
    instructions = parse_input(input)
    on_lights = set()
    for instruction in instructions:
        for x in range(instruction.x_min, instruction.x_max + 1):
            for y in range(instruction.y_min, instruction.y_max + 1):
                for z in range(instruction.z_min, instruction.z_max + 1):
                    coord = (x,y,z)
                    if instruction.toggle == 'on':
                        on_lights.add(coord)
                    elif instruction.toggle == 'off' and coord in on_lights:
                        on_lights.remove(coord)
    return len(on_lights)

'''
Theory:
Track on lights as box ranges
When switching lights off, find the intersection with any other boxes, and mark the intersection
When switching lights on, remove the off lights if relevant
Work out the volumes
'''
def count_active_everywhere(input):
    instructions = parse_input(input)
    instructions.reverse()
    previous = []
    total_count = 0
    for instr in instructions:
        if instr.toggle == 'on':
            size = get_volume_of_remainder(instr, previous)
            total_count += size
        previous.append(instr)
    return total_count

def get_volume_of_remainder(instr, previous):
    overlaps = []
    for prev in previous:
        overlap = find_overlap(instr, prev)
        if overlap:
            overlaps.append(overlap)
    overlap_size = 0
    for o1_idx in range(len(overlaps)):
        overlap_size += get_new_overlap_size(o1_idx, overlaps)

    return get_volume(instr) - overlap_size

def get_new_overlap_size(o_idx, overlaps):
    o = overlaps[o_idx]
    my_size = get_volume(o)
    total_overlap_with_overlaps = 0

    new_overlaps = []
    for n in range(o_idx):
        prev = overlaps[n]
        overlap = find_overlap(o, prev)
        if overlap:
            new_overlaps.append(overlap)

    for o2_idx in range(len(new_overlaps)):
        total_overlap_with_overlaps += get_new_overlap_size(o2_idx, new_overlaps)

        
    return my_size - total_overlap_with_overlaps

def get_volume(box):
    b = box
    x_length = b.x_max + 1 - b.x_min
    y_length = b.y_max + 1 - b.y_min
    z_length = b.z_max + 1 - b.z_min
    return x_length * y_length * z_length 

def is_overlapping(box_1, box_2):
    x_overlaps = box_1.x_max >= box_2.x_min and box_1.x_min <= box_2.x_max
    y_overlaps = box_1.y_max >= box_2.y_min and box_1.y_min <= box_2.y_max
    z_overlaps = box_1.z_max >= box_2.z_min and box_1.z_min <= box_2.z_max
    return x_overlaps and y_overlaps and z_overlaps

def find_overlap(box_1, box_2):
    if not is_overlapping(box_1, box_2):
        return None
    overlap_x = max(box_1.x_min, box_2.x_min), min(box_1.x_max, box_2.x_max)
    overlap_y = max(box_1.y_min, box_2.y_min), min(box_1.y_max, box_2.y_max)
    overlap_z = max(box_1.z_min, box_2.z_min), min(box_1.z_max, box_2.z_max)
    return Overlap(overlap_x, overlap_y, overlap_z)

class Overlap():
    def __init__(self, overlap_x, overlap_y, overlap_z):
        self.x_min = overlap_x[0]
        self.x_max = overlap_x[1]
        self.y_min = overlap_y[0]
        self.y_max = overlap_y[1]
        self.z_min = overlap_z[0]
        self.z_max = overlap_z[1]

    def __repr__(self):
        return f"x={self.x_min}..{self.x_max},y={self.y_min}..{self.y_max},z={self.z_min}..{self.z_max}"

class Instruction():
    def __init__(self, line):
        sections = line.split()
        self.toggle = sections[0]
        x_range, y_range, z_range = sections[1].split(',')
        x_parts = x_range.split('..')
        self.x_min = int(x_parts[0][2:])
        self.x_max = int(x_parts[1])
        y_parts = y_range.split('..')
        self.y_min = int(y_parts[0][2:])
        self.y_max = int(y_parts[1])
        z_parts = z_range.split('..')
        self.z_min = int(z_parts[0][2:])
        self.z_max = int(z_parts[1])
    
    def is_valid(self):
        return abs(self.x_min) <= 50 and abs(self.x_max) <= 50 and abs(self.y_min) <= 50 \
            and abs(self.y_max) <= 50 and abs(self.z_min) <= 50 and abs(self.z_max) <= 50
    
    def __repr__(self):
        return f"x={self.x_min}..{self.x_max},y={self.y_min}..{self.y_max},z={self.z_min}..{self.z_max}"

def parse_input(input):
    return [Instruction(line) for line in input]