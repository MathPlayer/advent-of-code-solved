#!/usr/bin/env python

import random


def read(filename):
    return open(filename).read()


def parse(data):
    first = True
    wires = {}
    gates = {}
    for line in data.splitlines():
        if not line.strip():
            first = False
            continue
        if first:
            wire, value = line.split(': ')
            wires[wire] = int(value)
        else:
            wire1, op, wire2, _, wire_out = line.split(' ')
            gates[wire_out] = (wire1, op, wire2)

    return (wires, gates)


def compute(out, wires, gates, depth=0):
    if depth > len(wires) + len(gates):
        raise RuntimeError('Possible circular dependency detected')
    if out in wires:
        return wires[out]
    wire1, op, wire2 = gates[out]
    val1 = compute(wire1, wires, gates, depth + 1)
    val2 = compute(wire2, wires, gates, depth + 1)
    if op == 'AND':
        result = val1 & val2
    elif op == 'OR':
        result = val1 | val2
    elif op == 'XOR':
        result = val1 ^ val2
    else:
        raise ValueError(f'Unknown operation: {op}')
    wires[out] = result
    return result


def get_int_from_wires(wires, letter):
    letter_wires = sorted((wire for wire in wires if wire.startswith(letter)), reverse=True)
    binary = ''.join(str(wires[wire] & 1) for wire in letter_wires)
    return int(binary, 2)


def part1(wires, gates):
    for wire in gates:
        compute(wire, wires, gates)

    print(get_int_from_wires(wires, 'z'))


def validate_up_to_bit(wires, gates, x, y, bit_count):
    local_wires = wires.copy()
    local_gates = gates.copy()

    z_expected = x + y
    z_wires_expected = [f'z{i:02d}' for i in range(bit_count)]  # Assume max 100 bits

    try:
        for wire in z_wires_expected:
            compute(wire, local_wires, local_gates)
        z_computed = get_int_from_wires(local_wires, 'z')
        ret = (z_expected & ((1 << bit_count) - 1)) == (z_computed & ((1 << bit_count) - 1))
        return ret
    except RuntimeError:
        return False
    except ValueError:
        return False


def alter_wires_from_int(wires, letter, value):
    for wire in (w for w in wires if w.startswith(letter)):
        tag = int(wire[1:])
        bit = (value >> tag) & 1
        wires[wire] = bit


def get_bit_len(wires, letter):
    return len([wire for wire in wires if wire.startswith(letter)])


def test_up_to_bit(wires, gates, bit_count, test_count=100):
    x_bit_len = get_bit_len(wires, 'x')
    y_bit_len = get_bit_len(wires, 'y')
    for i in range(test_count):
        x = random.randint(0, (1 << x_bit_len) - 1)
        y = random.randint(0, (1 << y_bit_len) - 1)

        alter_wires_from_int(wires, 'x', x)
        alter_wires_from_int(wires, 'y', y)

        if not validate_up_to_bit(wires, gates, x, y, bit_count):
            return False

    # Assume wiring is good after test_count successful tests
    return True


def part2(wires, gates, swap_count):
    z_bit_len = get_bit_len(gates.keys(), 'z')
    gate_names = set(gates.keys())

    swaps = set()

    print("Starting part 2")
    for bit_count in range(1, z_bit_len + 1):
        print(f">>> Test {bit_count=}")
        result = test_up_to_bit(wires, gates, bit_count)
        if result:
            print("OK")
            continue
        print("Need to find swaps")

        swap_found = False
        # Try all possible swaps:
        for i, a in enumerate(gate_names):
            if swap_found:
                break
            if a in swaps:
                continue
            for j, b in enumerate(gate_names):
                if i >= j:
                    continue
                if b in swaps:
                    continue
                gates[a], gates[b] = gates[b], gates[a]

                test = test_up_to_bit(wires, gates, bit_count)

                if test:
                    print(f"Swap {a} <-> {b} successful for {bit_count=}")
                    swaps.add(a)
                    swaps.add(b)
                    swap_found = True
                    break
                else:
                    # Swap back
                    gates[a], gates[b] = gates[b], gates[a]

        if not swap_found:
            raise RuntimeError(f"Could not find swap for {bit_count=}, maybe increase test_count?")

    print(','.join(sorted(swaps)))


if __name__ == '__main__':
    # PART1

    # filename = 'test1'
    # filename = 'test2'
    filename = 'input'
    raw = read(filename)
    wires, gates = parse(raw)

    part1(wires, gates)

    # PART 2
    filename = 'input'
    swap_count = 4

    raw = read(filename)
    wires, gates = parse(raw)

    part2(wires, gates, swap_count)
