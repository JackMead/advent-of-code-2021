from src.helpers.files import load_txt_file
from src.helpers.perf import add_profile

def run():
    input = load_txt_file('./src/day_19/input.txt')
    count, dist = count_beacons_and_dist(input)
    print(f"Day 19 Q1: there are {count} beacons")

    print(f"Day 19 Q2: the furthest scanners are {dist} apart")
        
@add_profile
def count_beacons_and_dist(input):
    scanners = parse_input(input)
    match_scanners(scanners)
    beacons = get_actual_beacons(scanners)
    dist = get_max_manhattan_dist_between_scanners(scanners)
    return len(beacons), dist

def get_max_manhattan_dist_between_scanners(scanners):
    max_dist = None
    for idx_s0 in range(len(scanners)):
        for idx_s1 in range(idx_s0 + 1, len(scanners)):
            s0 = scanners[idx_s0]
            s1 = scanners[idx_s1]
            dist = abs(s0.x - s1.x) + abs(s0.y - s1.y) + abs(s0.z - s1.z)
            if not max_dist or dist > max_dist:
                max_dist = dist
    return max_dist

def match_scanners(scanners):
    dont_match = []
    while(any_scanner_unmatched(scanners)):
        for i in range(len(scanners)):
            for j in range(i + 1, len(scanners)):
                if (i,j) in dont_match:
                    continue
                could_match = try_match_scanner_pair(scanners[i], scanners[j])
                if not could_match:
                    dont_match.append((i,j))

def any_scanner_unmatched(scanners):
    return any([not scanner.is_located() for scanner in scanners])

def try_match_scanner_pair(a, b):
    if a.is_located() == b.is_located():
        return True
    known = [s for s in [a,b] if s.is_located()][0]
    unknown = [s for s in [a,b] if not s.is_located()][0]

    # theory - iterate over all pairs of beacons, and see if diff is consistent
    # if so, hypothesise and see if others match
    matched = get_matching_beacons(known, unknown)

    if len(matched) >= 12:
        determine_unknown(matched, unknown)
        return True
    else:
        return False

def determine_unknown(matched, unknown):
    for x in get_coord_lambdas():
        for y in get_coord_lambdas():
            for z in get_coord_lambdas():
                kb1 = matched[0][0]
                ub1 = matched[0][1]
                poss_position = (kb1.c1 - x(ub1), kb1.c2 - y(ub1), kb1.c3 - z(ub1))
                valid = True
                for el in matched:
                    kbi, ubi = el
                    if kbi.c1 != poss_position[0] + x(ubi):
                        valid = False
                        break
                    if kbi.c2 != poss_position[1] + y(ubi):
                        valid = False
                        break
                    if kbi.c3 != poss_position[2] + z(ubi):
                        valid = False
                        break
                if valid:
                    print(f"Matched {unknown.id}")
                    print(f"New pos = {poss_position}")
                    unknown.rearrange(poss_position, x, y, z)
                    return


def get_matching_beacons(known, unknown):
    kb = known.beacons
    ub = unknown.beacons
    matched = []
    for idx_k1 in range(len(kb)):
        k1 = kb[idx_k1]
        if k1 in [m[0] for m in matched]:
            continue
        count = 0
        matched_unknown = []
        matched_other = None
        for idx_k2 in range(len(kb)):
            if idx_k1 == idx_k2:
                continue
            for idx_u1 in range(len(ub)):
                for idx_u2 in range(idx_u1 + 1, len(ub)):
                    k2 = kb[idx_k2]
                    u1 = ub[idx_u1]
                    u2 = ub[idx_u2]
                    success = match_beacons(k1, k2, u1, u2)
                    if success and count == 0:
                        matched_unknown.append(u1)
                        matched_unknown.append(u2)
                        matched_other = k2
                        count = 1
                    elif success and count == 1:
                        count = 2
                        if u1 in matched_unknown:
                            matched.append((k1, u1))
                            other_unknown = [o for o in matched_unknown if o != u1][0]
                            matched.append((matched_other, other_unknown))
                            matched.append((k2, u2))
                        else:
                            matched.append((k1, u2))
                            other_unknown = [o for o in matched_unknown if o != u2][0]
                            matched.append((matched_other, other_unknown))
                            matched.append((k2, u1))
                        break
                if count > 1:
                    break
            if count > 1:
                break
        if len(matched) >= 12:
            break
    return matched

def get_coord_lambdas():
    return [
        lambda b: b.c1,
        lambda b: -b.c1,
        lambda b: b.c2,
        lambda b: -b.c2,
        lambda b: b.c3,
        lambda b: -b.c3
    ]

def match_beacons(k1, k2, u1, u2):
    known_diffs = [k1.c1 - k2.c1, k1.c2 - k2.c2, k1.c3 - k2.c3]
    unknown_diffs = [u1.c1 - u2.c1, u1.c2 - u2.c2, u1.c3 - u2.c3]
    return diffs_match(known_diffs, unknown_diffs)
    
def add_match(match, coord, k, unknowns):
    if k in unknown_diffs:
        index = unknown_diffs.index(k)
        match[coord] = index
    else:
        index = unknown_diffs.index((-1) * k)
        match[coord] = -index

def diffs_match(d1, d2):
    for d in d1:
        if d not in d2 and (-d) not in d2:
            return False
    return True

def get_actual_beacons(scanners):
    all_beacons = {beacon for scanner in scanners for beacon in scanner.beacons}
    return all_beacons

def parse_input(input):
    scanners = []
    scanner_lines = []
    for line in input:
        if line.strip() == '':
            scanners.append(parse_scanner(scanner_lines))
            scanner_lines = []
        else:
            scanner_lines.append(line)
    scanners.append(parse_scanner(scanner_lines))
    
    return scanners

def parse_scanner(beacons):
    return Scanner(beacons)

class Beacon():
    def __init__(self, input_line):
        self.c1, self.c2, self.c3 = [int(num) for num in input_line.split(',')]

    def __eq__(self, other):
        if isinstance(other, Beacon):
            return self.c1 == other.c1 and self.c2 == other.c2 and self.c3 == other.c3
        return False

    def __hash__(self):
        return (self.c1, self.c2, self.c3).__hash__()

    def __str__(self):
        return str((self.c1, self.c2, self.c3))

class Scanner():
    def __init__(self, input_lines):
        self.id = input_lines[0].split()[2]
        self.beacons = [Beacon(input_line) for input_line in input_lines[1:]]
        ## TODO?
        if self.id == '0':
            self.position = (0,0,0)
        else:
            self.position = None

    def is_located(self):
        return self.position != None

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def z(self):
        return self.position[2]

    def rearrange(self, position, x, y, z):
        self.position = position
        for beacon in self.beacons:
            c1, c2, c3 = x(beacon) + position[0], y(beacon) + position[1], z(beacon) + position[2]
            beacon.c1, beacon.c2, beacon.c3 = c1, c2, c3