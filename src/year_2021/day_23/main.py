from src.helpers.files import load_txt_file
import networkx as nx
from src.helpers.perf import add_profile

'''
Graph captures below:

#############
#abcdefghijk#
###l#n#p#r###
  #m#o#q#s#
  #########


'''

def get_default_graph():
    graph = nx.Graph()
    graph.add_edge('a','b')
    graph.add_edge('b','c')
    graph.add_edge('c','d')
    graph.add_edge('d','e')
    graph.add_edge('e','f')
    graph.add_edge('f','g')
    graph.add_edge('g','h')
    graph.add_edge('h','i')
    graph.add_edge('i','j')
    graph.add_edge('j','k')

    graph.add_edge('c','l')
    graph.add_edge('e','n')
    graph.add_edge('g','p')
    graph.add_edge('i','r')

    graph.add_edge('l','m')
    graph.add_edge('n','o')
    graph.add_edge('p','q')
    graph.add_edge('r','s')

    for node in 'abcdefghijk':
        graph.nodes[node]['room'] = 'main'
    graph.nodes['l']['room'] = 'h1'
    graph.nodes['m']['room'] = 'h1'
    graph.nodes['n']['room'] = 'h2'
    graph.nodes['o']['room'] = 'h2'
    graph.nodes['p']['room'] = 'h3'
    graph.nodes['q']['room'] = 'h3'
    graph.nodes['r']['room'] = 'h4'
    graph.nodes['s']['room'] = 'h4'
    return graph

#############
#abcdefghijk#
###l#n#p#r###
  #m#o#q#s#
  #t#v#x#z#
  #u#w#y#$#
  #########
def get_extended_default_graph():
    graph = get_default_graph()
    graph.add_edge('m', 't')
    graph.add_edge('t', 'u')
    
    graph.add_edge('o', 'v')
    graph.add_edge('v', 'w')
    
    graph.add_edge('q', 'x')
    graph.add_edge('x', 'y')
    
    graph.add_edge('s', 'z')
    graph.add_edge('z', '$')
    graph.nodes['t']['room'] = 'h1'
    graph.nodes['u']['room'] = 'h1'
    graph.nodes['v']['room'] = 'h2'
    graph.nodes['w']['room'] = 'h2'
    graph.nodes['x']['room'] = 'h3'
    graph.nodes['y']['room'] = 'h3'
    graph.nodes['z']['room'] = 'h4'
    graph.nodes['$']['room'] = 'h4'
    return graph

hall_nodes = ['lmtu', 'novw', 'pqxy', 'rsz$']

halls = {
    'h1': 'lmtu',
    'h2': 'novw',
    'h3': 'pqxy',
    'h4': 'rsz$',
    'main': 'abcdefghijk'
}

room_owner = {
    'h1': 'A',
    'h2': 'B',
    'h3': 'C',
    'h4': 'D',
    'main': None
}

def run():
    input = load_txt_file('./src/year_2021/day_23/input.txt')
    energy = get_energy_required_to_organise(input)
    print(f"Day 23 Q1: min energy required = {energy}")
    full_energy = get_full_energy_required_to_organise(input)
    print(f"Day 23 Q2: min energy required = {full_energy}")

def get_energy_required_to_organise(lines):
    # start by finding a valid solution, don't worry about energy
    starting_places = parse_input(lines)
    seen = {
        graph_as_positions(starting_places): 0
    }
    places_to_consider = [starting_places]
    while (len(places_to_consider) > 0):
        if len(seen) % 100 == 0:
            print(f"Queue to consider: {len(places_to_consider)}")
            print(f"Total seen: {len(seen)}")
        origin = places_to_consider.pop(0)
        new_places_and_costs = get_all_possible_moves(origin)
        origin_pos = graph_as_positions(origin)
        current_energy = seen[origin_pos]
        for place in new_places_and_costs:
            positions = graph_as_positions(place[0])
            if positions not in seen or current_energy + place[1] < seen[positions]:
                seen[positions] = current_energy + place[1]
                if (seen[positions] < 15000):
                    places_to_consider.append(place[0])

    complete = [g for g in seen.keys() if finished_pos(g)]
    return min([seen[c] for c in complete])

def get_full_energy_required_to_organise(lines):
    # start by finding a valid solution, don't worry about energy
    starting_places = parse_input_new(lines)
    display_graph(starting_places)
    seen = {
        graph_as_positions(starting_places): 0
    }
    places_to_consider = [starting_places]
    while (len(places_to_consider) > 0):
        if len(seen) % 100 == 0:
            print(f"Queue to consider: {len(places_to_consider)}")
            print(f"Total seen: {len(seen)}")
        origin = places_to_consider.pop()
        new_places_and_costs = get_all_possible_moves(origin)
        origin_pos = graph_as_positions(origin)
        current_energy = seen[origin_pos]
        for place in new_places_and_costs:
            positions = graph_as_positions(place[0])
            if positions not in seen or current_energy + place[1] < seen[positions]:
                seen[positions] = current_energy + place[1]
                if (seen[positions] < 50000):
                    places_to_consider.append(place[0])

    complete = [g for g in seen.keys() if finished_pos(g)]
    return min([seen[c] for c in complete])

def graph_as_positions(g):
    a = []
    b = []
    c = []
    d = []
    for n in g.nodes:
        owner = g.nodes[n].get('occupied')
        if owner == 'A':
            a.append(n)
        elif owner == 'B':
            b.append(n)
        elif owner == 'C':
            c.append(n)
        elif owner == 'D':
            d.append(n)
    return (
        tuple(a),
        tuple(b),
        tuple(c),
        tuple(d)
    )

def is_unfinished(places):
    for node_id in places.nodes:
        node = places.nodes[node_id]
        if node['room'] == 'main' and node.get('occupied'):
            return True
        if node['room'] == 'h1' and not node.get('occupied') == 'A':
            return True
        if node['room'] == 'h2' and not node.get('occupied') == 'B':
            return True
        if node['room'] == 'h3' and not node.get('occupied') == 'C':
            return True
        if node['room'] == 'h4' and not node.get('occupied') == 'D':
            return True
    return False

def finished_pos(pos):
    for i in range(len(pos)):
        for el in pos[i]:
            if el not in hall_nodes[i]:
                return False
    return True

def get_all_possible_moves(places):
    if not is_unfinished(places):
        return []
    moves = []
    for node_id in places.nodes:
        start_node = places.nodes[node_id]

        if start_node.get('occupied') != None and can_move_from(node_id, places):
            pod_type = start_node.get('occupied')
            for target_node_id in places.nodes:
                target_node = places.nodes[target_node_id]
                if node_id == target_node_id or target_node.get('occupied') != None:
                    continue
                if is_valid_target(node_id, target_node_id, pod_type, places):
                    path = shortest_path(node_id, target_node_id, places)
                    if is_valid_path(start_node, path, places):
                        copy = make_copy(places)
                        perform_move(node_id, target_node_id, copy)
                        cost = (len(path) - 1) * get_energy_cost_per_move(pod_type)
                        moves.append((copy, cost)) 
    return moves

fastest_paths = {}
def shortest_path(node_id, target_node_id, places):
    key = (node_id, target_node_id)
    if key in fastest_paths:
        return fastest_paths[key]
    new_path = nx.shortest_path(places, node_id, target_node_id)
    fastest_paths[key] = new_path
    return new_path

def can_move_from(start_node_id, places):
    start_room = get_room_from_node(start_node_id)
    pod_type = places.nodes[start_node_id].get('occupied')

    if start_room != 'main':
        matching_hall = [n for n in hall_nodes if start_node_id in n][0]
        i = matching_hall.index(start_node_id)
        for j in range(0, i):
            if places.nodes[matching_hall[j]].get('occupied') != None:                
                return False

    if room_owner[start_room] == pod_type:
        matching_hall = [n for n in hall_nodes if start_node_id in n][0]
        i = matching_hall.index(start_node_id)
        all_same_type_below = True
        for j in range(i + 1, len(matching_hall)):
            other_space = matching_hall[j]
            lower_node = places.nodes.get(other_space)
            if lower_node == None:
                break
            if lower_node.get('occupied') != pod_type:
                all_same_type_below = False
                break
        if all_same_type_below:
            return False
    return True

def perform_move(start_node_id, target_node_id, copy):
    start_node = copy.nodes[start_node_id]
    target_node = copy.nodes[target_node_id]
    target_node['occupied'] = start_node['occupied']
    start_node.pop('occupied', None)

def make_copy(places):
    return places.copy()

def is_valid_target(start_node_id, target_node_id, pod_type, places):
    main_room_nodes = 'abcdefghijk'
    start_room = get_room_from_node(start_node_id)
    end_room = get_room_from_node(target_node_id)
    # can't finish in front of hall
    if target_node_id in ['c', 'e', 'g', 'i']:
        return False
    # can't move within corridor
    if start_room == end_room:
        return False
    # can't enter hall that has the wrong type in it
    if end_room != 'main':
        matching_hall = [n for n in hall_nodes if target_node_id in n][0]
        i = matching_hall.index(target_node_id)
        invalid = False
        for j in range(i + 1, len(matching_hall)):
            other_space = matching_hall[j]
            other_node = places.nodes.get(other_space)
            if other_node == None:
                break
            if other_node.get('occupied') != pod_type:
                invalid = True
                break
        if invalid:
            return False     
    # can't move to another hallway
    if room_owner[end_room] not in [None, pod_type]:
        return False
    return True

rooms = {
    'l': 'h1',
    'm': 'h1',
    't': 'h1',
    'u': 'h1',
    'n': 'h2',
    'o': 'h2',
    'v': 'h2',
    'w': 'h2',
    'p': 'h3',
    'q': 'h3',
    'x': 'h3',
    'y': 'h3',
    'r': 'h4',
    's': 'h4',
    'z': 'h4',
    '$': 'h4'
}
for c in 'abcdefghijk':
    rooms[c] = 'main'

def get_room_from_node(node):
    return rooms[node]

def is_valid_path(start_node, path, places):
    # can't move through another pod
    for node_id in path:
        if node_id == path[0]:
            continue
        if places.nodes[node_id].get('occupied'):
            return False
    return True

def parse_input(input):
    graph = get_default_graph()
    node_dict = {
        (2,3): 'l',
        (3,3): 'm',
        (2,5): 'n',
        (3,5): 'o',
        (2,7): 'p',
        (3,7): 'q',
        (2,9): 'r',
        (3,9): 's'
    }
    for hall in [3,5,7,9]:
        for row in [2,3]:
            pod_type = input[row][hall]
            node = node_dict[(row, hall)]
            graph.nodes[node]['occupied'] = pod_type
    return graph

def parse_input_new(input):
    graph = get_extended_default_graph()
    node_dict = {
        (2,3): 'l',
        (3,3): 'u',
        (2,5): 'n',
        (3,5): 'w',
        (2,7): 'p',
        (3,7): 'y',
        (2,9): 'r',
        (3,9): '$'
    }
    for hall in [3,5,7,9]:
        for row in [2,3]:
            pod_type = input[row][hall]
            node = node_dict[(row, hall)]
            graph.nodes[node]['occupied'] = pod_type
    graph.nodes['m']['occupied'] = 'D'
    graph.nodes['o']['occupied'] = 'C'
    graph.nodes['q']['occupied'] = 'B'
    graph.nodes['s']['occupied'] = 'A'
    graph.nodes['t']['occupied'] = 'D'
    graph.nodes['v']['occupied'] = 'B'
    graph.nodes['x']['occupied'] = 'A'
    graph.nodes['z']['occupied'] = 'C'

    return graph

def get_energy_cost_per_move(pod_type):
    return {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
    }[pod_type]

def display_graph(g):
    nodes = g.nodes
    print("Graph:")
    print("#############")
    string = '#'
    for char in 'abcdefghijk':
        string += (nodes[char].get('occupied', '.'))
    string += '#'
    print(string)
    print(f"###{nodes['l'].get('occupied', '.')}#{nodes['n'].get('occupied', '.')}#{nodes['p'].get('occupied', '.')}#{nodes['r'].get('occupied', '.')}###")
    print(f"  #{nodes['m'].get('occupied', '.')}#{nodes['o'].get('occupied', '.')}#{nodes['q'].get('occupied', '.')}#{nodes['s'].get('occupied', '.')}#")
    print(f"  #{nodes['t'].get('occupied', '.')}#{nodes['v'].get('occupied', '.')}#{nodes['x'].get('occupied', '.')}#{nodes['z'].get('occupied', '.')}#")
    print(f"  #{nodes['u'].get('occupied', '.')}#{nodes['w'].get('occupied', '.')}#{nodes['y'].get('occupied', '.')}#{nodes['$'].get('occupied', '.')}#")
    print("  #########")