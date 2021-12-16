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


def parse(raw):
    V = int(raw[:3], base=2)
    T = raw[3:6]
    i = 6

    if T == '100':
        # Parse literal
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


def sum_versions(packet):
    V, T, content, raw = packet
    ret = V
    if T == '100':
        return ret
    for c in content:
        ret += sum_versions(c)
    return ret


def hex_to_bin(packet):
    return ''.join([BITS[c] for c in packet])


def solve(hex_packet):
    print(sum_versions(parse(hex_to_bin(hex_packet))))


test_1 = 'D2FE28'
test_2 = '38006F45291200'
test_3 = 'EE00D40C823060'
test_4 = '8A004A801A8002F478'
packet = open('input.txt', 'r').read().strip()

print(parse(hex_to_bin(test_1)))
print(parse(hex_to_bin(test_2)))
print(parse(hex_to_bin(test_3)))
solve(test_4)
solve(packet)
