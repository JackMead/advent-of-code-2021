from src.helpers.files import load_txt_file
from functools import reduce

def run():
    input = load_txt_file('./src/year_2021/day_16/input.txt')
    version_sum = sum_packet_versions(input[0])
    print(f"Day 16 Q1: version sum = {version_sum}")
    value = get_packet_value(input[0])
    print(f"Day 16 Q2: value = {value}")

def sum_packet_versions(input):
    packets = get_packets(input)
    return total_version_sum(packets)

def get_packet_value(input_string):
    input_as_bits = get_input_as_bits(input_string)
    _, packet = get_packet_from_bits(input_as_bits)
    return packet.get_value()

class Packet():
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

class LiteralPacket(Packet):
    def __init__(self, version, type_id, literal_bit_string):
        super(LiteralPacket, self).__init__(version, type_id)
        self.literal_bit_string = literal_bit_string
        self.literal = int(literal_bit_string, 2)

    def get_len(self):
        literal_length = len(self.literal_bit_string)
        extra_bits_from_literal = (literal_length // 4) * 5
        return 6 + extra_bits_from_literal

    def get_value(self):
        return self.literal

class OperatorPacket(Packet):
    def __init__(self, version, type_id, length_type_id, sub_packets):
        super(OperatorPacket, self).__init__(version, type_id)
        self.length_type_id = length_type_id
        self.sub_packets = sub_packets
    
    def get_len(self):
        header_length = 22 if self.length_type_id == 0 else 18
        return header_length + sum([packet.get_len() for packet in self.sub_packets])

    def get_value(self):
        packet_values = [packet.get_value() for packet in self.sub_packets]
        if self.type_id == 0:
            return sum(packet_values)
        if self.type_id == 1:
            return reduce((lambda x, y: x * y), packet_values)
        if self.type_id == 2:
            return min(packet_values)
        if self.type_id == 3:
            return max(packet_values)
        if self.type_id == 5:
            return 1 if packet_values[0] > packet_values[1] else 0
        if self.type_id == 6:
            return 1 if packet_values[0] < packet_values[1] else 0
        if self.type_id == 7:
            return 1 if packet_values[0] == packet_values[1] else 0
        raise Exception(f"Type id {self.type_id} not valid")

def get_packet_from_bits(bits):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    if type_id == 4:
        return get_literal_packet(version, type_id, bits)
    else:
        return get_operator_packet(version, type_id, bits)

def get_literal_packet(version, type_id, bits):
    reading_from_bit = 6
    bit_string = ""
    while(bits[reading_from_bit] == '1'):
        bit_string += bits[reading_from_bit + 1: reading_from_bit + 5]
        reading_from_bit += 5
    bit_string += bits[reading_from_bit + 1: reading_from_bit + 5]
    first_unused_bit = reading_from_bit + 5
    return first_unused_bit, LiteralPacket(version, type_id, bit_string)

class StopCondition():
    def __init__(self, condition, number):
        self.condition = condition
        self.number = number
    
    def is_met(self, num_packets, num_bits):
        if self.condition == 'PACKET_NUMBER':
            return self.number == num_packets
        else:
            return self.number == num_bits
        raise Exception("Packet lied")

def get_operator_packet(version, type_id, bits):
    length_type_id = int(bits[6])
    condition = 'PACKET_LENGTH' if length_type_id == 0 else 'PACKET_NUMBER'
    condition_value = bits[7:22] if length_type_id == 0 else bits[7:18]
    stop_condition = StopCondition(condition, int(condition_value, 2))

    starting_bit = 22 if length_type_id == 0 else 18
    num_packets = 0
    num_bits = 0
    sub_packets = []
    while(not stop_condition.is_met(num_packets, num_bits)):
        starting_bit, packet = return_next_internal_packet(starting_bit, bits)
        num_packets += 1
        num_bits += packet.get_len()
        sub_packets.append(packet)

    first_unused_bit = starting_bit
    return first_unused_bit, OperatorPacket(version, type_id, length_type_id, sub_packets)

def return_next_internal_packet(starting_bit, bits):
    first_unused_bit, packet = get_packet_from_bits(bits[starting_bit:])
    return starting_bit + first_unused_bit, packet

def get_input_as_bits(input_string):
    hex_size = len(input_string) 
    final_bin_size = hex_size * 4
    binary_string = bin(int(input_string, 16))[2:]
    padded_binary = binary_string.zfill(final_bin_size)
    return padded_binary

def get_packets(input_string):
    input_as_bits = get_input_as_bits(input_string)
    _, packet = get_packet_from_bits(input_as_bits)
    packets = [packet]
    subs = [] if isinstance(packet, LiteralPacket) else packet.sub_packets
    while (len(subs) > 0):
        sub = subs.pop()
        packets.append(sub)
        if isinstance(sub, OperatorPacket):
            subs += sub.sub_packets
    
    return packets

def total_version_sum(packets):
    return sum([packet.version for packet in packets])