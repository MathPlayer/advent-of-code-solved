#!/usr/bin/env python3

ROCK = 'O'
WALL = '#'
SPACE = '.'


def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    platform = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line.strip()):
            platform[(row, col)] = char

    return platform, len(lines), len(lines[0].strip())


def print_platform(platform, rows, cols):
    for row in range(rows):
        for col in range(cols):
            print(platform[(row, col)], end='')
        print()


def roll_rocks(platform, rows, cols):
    for col in range(cols):
        last_fixed = -1
        for row in range(rows):
            if platform[(row, col)] == SPACE:
                continue
            if platform[(row, col)] == WALL:
                last_fixed = row
                continue
            if platform[(row, col)] == ROCK:
                if last_fixed < row - 1:
                    last_fixed += 1
                    platform[(last_fixed, col)] = ROCK
                    platform[(row, col)] = SPACE
                else:
                    last_fixed = row


def get_load(platform, rows, cols):
    load = 0
    for (row, col), value in platform.items():
        if value == ROCK:
            # print(row, col, "Adding load", rows - row)
            load += (rows - row)
    return load


def solve():
    filename = 'test'
    filename = 'input'

    platform, rows, cols = read_matrix(filename)
    print_platform(platform, rows, cols)
    print("ROLLING")
    roll_rocks(platform, rows, cols)
    print_platform(platform, rows, cols)

    load = get_load(platform, rows, cols)
    print(load)



solve()
