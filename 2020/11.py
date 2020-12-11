#!/usr/bin/env python

import sys

from copy import deepcopy

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

DIRECTIONS = tuple((x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y)

def read(in_file):
    ''' Reads data for day 11. '''
    with open(in_file) as f:
        data = list(map(lambda x: [c for c in x.strip()], f.readlines()))
    return data


def part_1_step(data):
    new_data = deepcopy(data)
    width = len(data[0])
    height = len(data)

    for y in range(height):
        for x in range(width):
            if data[y][x] == FLOOR:
                continue
            count = 0
            neigh = 0
            for i, j in DIRECTIONS:
                if x + i < 0 or x + i >= width:
                    continue
                if y + j < 0 or y + j >= height:
                    continue
                neigh += 1
                if data[y][x] == EMPTY and data[y + j][x + i] != OCCUPIED:
                    count += 1
                if data[y][x] == OCCUPIED and data[y + j][x + i] == OCCUPIED:
                    count += 1
            if data[y][x] == EMPTY and count == neigh:
                new_data[y][x] = OCCUPIED
            if data[y][x] == OCCUPIED and count >= 4:
                new_data[y][x] = EMPTY
    return new_data


def part_2_step(data):
    new_data = deepcopy(data)
    width = len(data[0])
    height = len(data)

    for y in range(height):
        for x in range(width):
            if data[y][x] == FLOOR:
                continue
            count = 0
            neigh = 0
            for i, j in DIRECTIONS:
                if x + i < 0 or x + i >= width:
                    continue
                if y + j < 0 or y + j >= height:
                    continue
                new_neigh = False
                pos_x = x
                pos_y = y
                while True:
                    pos_x += i
                    pos_y += j
                    if pos_x < 0 or pos_x >= width:
                        break
                    if pos_y < 0 or pos_y >= height:
                        break
                    if data[pos_y][pos_x] == FLOOR:
                        continue
                    new_neigh = True
                    if data[y][x] == EMPTY and data[pos_y][pos_x] != OCCUPIED and data[pos_y][pos_x] != FLOOR:
                        count += 1
                        break
                    if data[y][x] == OCCUPIED and data[pos_y][pos_x] == OCCUPIED:
                        count += 1
                        break
                    if data[pos_y][pos_x] != FLOOR:
                        break
                if new_neigh:
                    neigh += 1

            if data[y][x] == EMPTY and count == neigh:
                new_data[y][x] = OCCUPIED
            if data[y][x] == OCCUPIED and count >= 5:
                new_data[y][x] = EMPTY
    return new_data


def solve(in_file):
    ''' Solves day 11. '''
    print(in_file)
    data = read(in_file)

    # part 1
    part_1_data = deepcopy(data)
    i = 0
    while True:
        i += 1
        if not i % 10:
            print(f"D: Step {i}")
        new_data = part_1_step(part_1_data)
        if new_data == part_1_data:
            print(f"D: Found at step {i}")
            break
        part_1_data = new_data
    print(sum(map(lambda x: x.count(OCCUPIED), part_1_data)))

    # part 2
    part_2_data = deepcopy(data)
    i = 0
    while True:
        i += 1
        if not i % 10:
            print(f"D: Step{i}")
        new_data = part_2_step(part_2_data)
        if new_data == part_2_data:
            print(f"D: Found at step {i}")
            break
        part_2_data = new_data
    print(sum(map(lambda x: x.count(OCCUPIED), part_2_data)))


if __name__ == '__main__':
    solve('11test.in')
    solve('11.in')

    sys.exit(0)
