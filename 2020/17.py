#!/usr/bin/env python

import re
import sys

ACTIVE = '#'
INACTIVE = '.'

def read(in_file):
    ''' Reads data for day 15. '''
    data = {}
    with open(in_file) as f:
        for y, line in enumerate(map(lambda x: x.strip(), f.readlines())):
            for x, c in enumerate(line):
                data[(x, y)] = c

    return data


def add_coords(a, b):
    ''' Computes (a[0] + b[0], a[1] + b[1], ...). '''
    return tuple(map(sum, zip(a, b)))


def count_active(directions, data, coord):
    ''' Counts how many neighbors of a given coord are ACTIVE in the given data. '''
    count = 0
    for d in directions:
        neigh = add_coords(coord, d)
        if data.get(neigh, INACTIVE) == ACTIVE:
            count += 1
    return count


def new_value(data, coord, count):
    ''' Determines the new value for the given coord and neighbor coun in the given data. '''
    v = data.get(coord, INACTIVE)
    if v == ACTIVE and 2 <= count <= 3:
        return ACTIVE
    elif v == INACTIVE and count == 3:
        return ACTIVE
    else:
        return INACTIVE


def cycle(directions, data):
    ''' Runs a cycle of the multidimensional Conway's game of life variation. '''
    new_data = {}

    # Update existing data.
    for coord in data:
        count = count_active(directions, data, coord)
        new_data[coord] = new_value(data, coord, count)

    # Check outside of existing data for new ACTIVE.
    for coord in data:
        for d in directions:
            neigh = add_coords(coord, d)
            if neigh in data:
                # Done in prev step.
                continue
            count = count_active(directions, data, neigh)
            neigh_value = new_value(data, neigh, count)
            # Expand only if needed.
            if neigh_value == ACTIVE:
                new_data[neigh] = ACTIVE

    return new_data


def solve(in_file, cycles):
    ''' Solves day 16. '''
    data = read(in_file)
    print(f"--- {in_file}")

    # Part 1: 3 dimensions are fast
    DIRECIONS_1 = [(x, y, z)
        for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)
        if x != 0 or y != 0 or z != 0]
    part1 = {(x, y, 0): v for (x, y), v in data.items()}
    for i in range(cycles):
        print(f"Part 1 step: {i+1}")
        part1 = cycle(DIRECIONS_1, part1)
    print(sum(x == ACTIVE for x in part1.values()))

    # Part 2: 4 dimensions are slow
    DIRECIONS_2 = [(x, y, z, w)
        for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for w in range(-1, 2)
        if x != 0 or y != 0 or z != 0 or w != 0]
    part2 = {(x, y, 0, 0): v for (x, y), v in data.items()}
    for i in range(cycles):
        print(f"Part 2 step: {i+1}")
        part2 = cycle(DIRECIONS_2, part2)
    print(sum(x == ACTIVE for x in part2.values()))


if __name__ == '__main__':
    solve('17test.in', 6)
    solve('17.in', 6)

    sys.exit(0)
