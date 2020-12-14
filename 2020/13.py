#!/usr/bin/env python

import sys


def read(in_file):
    ''' Reads data for day 13. '''
    with open(in_file) as f:
        data = tuple(map(lambda x: x.strip().split(","), f.readlines()))
    return data


def solve_1(data):
    ''' Solves part 1 of day 13. '''
    timestamp = int(data[0][0])
    buses = set()
    for ID in data[1]:
        try:
            buses.add(int(ID))
        except Exception:
            pass  # Ignore 'x'.

    departure = timestamp
    while True:
        departure += 1
        bus = next((ID for ID in buses if departure % ID == 0), None)
        if bus:
            print(bus * (departure - timestamp))
            return


def solve_2(data, guess=None):
    ''' Solves part 2 of day 13. '''
    buses = []
    for index, ID in enumerate(data[1]):
        if ID == 'x':
            continue
        buses.append((index, int(ID)))
    print(buses)
    from math import prod
    max_timestamp = prod(x[1] for x in buses)

    # Sort by bus frequencies
    buses = sorted(buses, key=lambda x: -x[1])
    print(buses)

    # Determine an interation step based on max 2 vlues.
    # Pop the values to avoid checking them later.
    delay_x, bus_x = buses.pop(0)
    delay_y, bus_y = buses.pop(0)

    # Find two values for T so that:
    # T + delay_x = bus_x * K
    # T + delay_y = bus_y * K
    T_candidates = []
    for T in range(bus_x * bus_y * 2):
        if (T + delay_x) % bus_x or (T + delay_y) % bus_y:
            continue
        print(f"Found T: {T} for delay_x {delay_x} bus_x {bus_x} delay_y {delay_y} bus_y {bus_y}")
        T_candidates.append(T)

    # We only need to check number of form "T_candidates[0] + K * (T_candidates[1] - T_candidates[0])"
    # Find first number below the guess.
    if guess:
        factor = guess // (T_candidates[1] - T_candidates[0]) - 1
        first = T_candidates[0] + factor * (T_candidates[1] - T_candidates[0])
        step = T_candidates[1] - T_candidates[0]
    else:
        first = T_candidates[0]
        step = T_candidates[1] - T_candidates[0]
    print(f"Debug: using first {first} and step {step}")
    timestamp = first
    debug_print = 0
    while timestamp <= max_timestamp:
        debug_print += 1
        if not debug_print % 1000000:
            print(f"Debug step {debug_print // 1000000} -> timestamp {timestamp}")
        timestamp += step
        if any((timestamp + delay) % bus for (delay, bus) in buses):
            continue
        print(f"Found timestamp {timestamp}")
        break

    # Most likely this brute-force can be improved:
    # - use the bus having delay 0.
    # - merge the computed candidate with the next buses in the list with the same rule.
    #
    # Anyhow, covid made it weird for me to try to optimize further, so I waited :)
    #
    # time ./13.py said:
    # ./13.py  1427.64s user 0.13s system 99% cpu 23:47.95 total


def solve(in_file, guess=None):
    ''' Solves day 13. '''
    print(in_file)
    data = read(in_file)
    solve_1(data)
    solve_2(data, guess)


if __name__ == '__main__':
    solve('13test.in')
    solve_2([[], '17,x,13,19'.split(',')])
    solve_2([[], '67,7,59,61'.split(',')])
    # solve('13.in', 100000000000000)

    sys.exit(0)
