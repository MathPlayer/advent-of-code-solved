#!/usr/bin/env python

import sys

from copy import deepcopy
from itertools import product

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

DIRECTIONS = tuple((x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y)

def read(in_file):
    ''' Reads data for day 11. '''
    with open(in_file) as f:
        data = list(map(lambda x: [c for c in x.strip()], f.readlines()))
    return data


def transform_1(data, height, width, y, x):
    old = data[y][x]
    if old == FLOOR:
        return old
    count = 0
    neigh = 0
    for i, j in DIRECTIONS:
        if not (0 <= x + i < width) or not (0 <= y + j < height):
            continue
        neigh += 1
        new = data[y + j][x + i]
        count += (old == EMPTY and new != OCCUPIED) or (old == OCCUPIED and new == OCCUPIED)
    if old == EMPTY and count == neigh:
        return OCCUPIED
    if old == OCCUPIED and count >= 4:
        return EMPTY
    return old


def transform_2(data, height, width, y, x):
    old = data[y][x]
    if old == FLOOR:
        return old
    count = 0
    neigh = 0
    for i, j in DIRECTIONS:
        if not (0 <= x + i < width) or not (0 <= y + j < height):
            continue
        new_neigh = False
        pos_x = x + i
        pos_y = y + j
        while 0 <= pos_x < width and 0 <= pos_y < height:
            new = data[pos_y][pos_x]
            if new != FLOOR:
                new_neigh = True
                # Update count as needed
                count += (old == EMPTY and new == EMPTY) or (old == OCCUPIED and new == OCCUPIED)
                break
            pos_x += i
            pos_y += j
        neigh += new_neigh


    if old == EMPTY and count == neigh:
        return OCCUPIED
    if old == OCCUPIED and count >= 5:
        return EMPTY
    return old


def step(data, width, height, transform):
    new_data = deepcopy(data)
    for y, x in product(range(height), range(width)):
        new_data[y][x] = transform(data, height, width, y, x)
    return new_data


def solve(in_file):
    ''' Solves day 11. '''
    print(in_file)
    data = read(in_file)
    width = len(data[0])
    height = len(data)

    # part 1
    part_data = deepcopy(data)
    i = 0
    while True:
        i += 1
        if not i % 10:
            print(f"D: Step {i}")
        new_data = step(part_data, width, height, transform_1)
        if new_data == part_data:
            print(f"D: Found at step {i}")
            break
        part_data = new_data
    print(sum(map(lambda x: x.count(OCCUPIED), part_data)))

    # part 2
    part_data = deepcopy(data)
    i = 0
    while True:
        i += 1
        if not i % 10:
            print(f"D: Step {i}")
        new_data = step(part_data, width, height, transform_2)
        if new_data == part_data:
            print(f"D: Found at step {i}")
            break
        part_data = new_data
    print(sum(map(lambda x: x.count(OCCUPIED), part_data)))


if __name__ == '__main__':
    solve('11test.in')
    solve('11.in')

    sys.exit(0)
