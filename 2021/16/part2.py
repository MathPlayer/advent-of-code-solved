from math import inf

BITS = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

LITERAL = 4
SUM = 0
PRODUCT = 1
MIN = 2
MAX = 3
GREATER_THAN = 5
LESS_THAN = 6
EQUAL = 7


def parse(raw):
    V = int(raw[:3], base=2)
    T = int(raw[3:6], base=2)
    i = 6

    if T == LITERAL:
        value = ''
        while True:
            bits = raw[i:i+5]
            value += bits[1:]
            i += 5
            if bits[0] == '0':
                break
        return V, T, int(value, base=2), raw[:i]
    else:
        mode = int(raw[i])
        i += 1
        if mode == 0:
            number_of_bits = int(raw[i:i+15], base=2)
            i += 15
            packets = []
            while number_of_bits:
                packet = parse(raw[i:])
                packets.append(packet)
                i += len(packet[-1])
                number_of_bits -= len(packet[-1])
            return V, T, packets, raw[:i]
        if mode == 1:
            packet_count = int(raw[i:i+11], base=2)
            i += 11
            packets = []
            for _ in range(packet_count):
                packet = parse(raw[i:])
                packets.append(packet)
                i += len(packet[-1])
            return V, T, packets, raw[:i]


def hex_to_bin(packet):
    return ''.join([BITS[c] for c in packet])


def compute_value(packet):
    V, T, content, raw = packet
    if T == LITERAL:
        ret = content
    if T == SUM:
        ret = 0
        for c in content:
            ret += compute_value(c)
    if T == PRODUCT:
        ret = 1
        for c in content:
            ret *= compute_value(c)
    if T == MIN:
        ret = inf
        for c in content:
            ret = min(ret, compute_value(c))
    if T == MAX:
        ret = 0
        for c in content:
            ret = max(ret, compute_value(c))
    if T == GREATER_THAN:
        v1, v2 = [compute_value(c) for c in content[:2]]
        ret = 1 if v1 > v2 else 0
    if T == LESS_THAN:
        v1, v2 = [compute_value(c) for c in content[:2]]
        ret = 1 if v1 < v2 else 0
    if T == EQUAL:
        v1, v2 = [compute_value(c) for c in content[:2]]
        ret = 1 if v1 == v2 else 0
    return ret


def solve(hex_packet):
    print(compute_value(parse(hex_to_bin(hex_packet))))


solve('C200B40A82')
solve('9C0141080250320F1802104A08')

packet = open('input.txt', 'r').read().strip()
solve(packet)
