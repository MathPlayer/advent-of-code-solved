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
    print("------")


def roll_rocks_north(platform, rows, cols):
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


def roll_rocks_west(platform, rows, cols):
    for row in range(rows):
        last_fixed = -1
        for col in range(cols):
            if platform[(row, col)] == SPACE:
                continue
            if platform[(row, col)] == WALL:
                last_fixed = col
                continue
            if platform[(row, col)] == ROCK:
                if last_fixed < col - 1:
                    last_fixed += 1
                    platform[(row, last_fixed)] = ROCK
                    platform[(row, col)] = SPACE
                else:
                    last_fixed = col


def roll_rocks_east(platform, rows, cols):
    for row in range(rows):
        last_fixed = cols
        for col in range(cols - 1, -1, -1):
            if platform[(row, col)] == SPACE:
                continue
            if platform[(row, col)] == WALL:
                last_fixed = col
                continue
            if platform[(row, col)] == ROCK:
                if last_fixed > col + 1:
                    last_fixed -= 1
                    platform[(row, last_fixed)] = ROCK
                    platform[(row, col)] = SPACE
                else:
                    last_fixed = col


def roll_rocks_south(platform, rows, cols):
    for col in range(cols):
        last_fixed = rows
        for row in range(rows - 1, -1, -1):
            if platform[(row, col)] == SPACE:
                continue
            if platform[(row, col)] == WALL:
                last_fixed = row
                continue
            if platform[(row, col)] == ROCK:
                if last_fixed > row + 1:
                    last_fixed -= 1
                    platform[(last_fixed, col)] = ROCK
                    platform[(row, col)] = SPACE
                else:
                    last_fixed = row


def spin(platform, rows, cols):
    roll_rocks_north(platform, rows, cols)
    roll_rocks_west(platform, rows, cols)
    roll_rocks_south(platform, rows, cols)
    roll_rocks_east(platform, rows, cols)


def get_load(platform, rows, cols):
    load = 0
    for (row, col), value in platform.items():
        if value == ROCK:
            # print(row, col, "Adding load", rows - row)
            load += (rows - row)
    return load


def get_hash(platform):
    return frozenset(platform.items())


def solve(platform, rows, cols):
    count = 1000000000
    states = {}
    step = 0
    while True:
        hash = get_hash(platform)
        if hash in states:
            cycle_start = states[hash][0]
            cycle_len = step - cycle_start
            break

        states[hash] = (step, get_load(platform, rows, cols))
        spin(platform, rows, cols)

        step += 1

    remaining_spins = (count - cycle_start) % cycle_len
    for _ in range(remaining_spins):
        spin(platform, rows, cols)

    print(get_load(platform, rows, cols))


filename = 'test'
filename = 'input'

platform, rows, cols = read_matrix(filename)

solve(platform, rows, cols)

print("DONE")
