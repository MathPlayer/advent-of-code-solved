#!/usr/bin/env python3

from copy import deepcopy

WALL = '#'
EMPTY = '.'
GUARD = '^'

DIRECTIONS = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}
ORDER = ['up', 'right', 'down', 'left']


def next_position(current, direction):
    return current[0] + DIRECTIONS[direction][0], current[1] + DIRECTIONS[direction][1]


def next_direction(direction):
    return ORDER[(ORDER.index(direction) + 1) % len(ORDER)]


def print_2d(grid):
    print("----------------------")
    min_x = min([x[0] for x in grid])
    max_x = max([x[0] for x in grid])
    min_y = min([x[1] for x in grid])
    max_y = max([x[1] for x in grid])

    for row in range(min_x, max_x + 1):
        for col in range(min_y, max_y + 1):
            print(grid[(row, col)], end='')
        print()


def print_2d_path(grid, path):
    print("----------------------")
    min_x = 0
    max_x = max([x[0] for x in grid])
    min_y = 0
    max_y = max([x[1] for x in grid])

    path_coords = set(x[0] for x in path)
    for row in range(min_x, max_x + 1):
        for col in range(min_y, max_y + 1):
            if (row, col) in path_coords:
                print('X', end='')
            else:
                print(grid[(row, col)], end='')
        print()


def read(filename):
    data = open(filename).readlines()
    data = [x.strip() for x in data]

    result = {}
    guard = None
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == GUARD:
                guard = (i, j)
                result[(i, j)] = EMPTY
            else:
                result[(i, j)] = c

    return guard, result


def part_1(data):
    guard, grid = data

    direction = 'up'
    VISITED = 'X'
    current = guard
    visited = set()
    while True:
        visited.add(current)
        grid[current] = VISITED

        next_pos = next_position(current, direction)
        if next_pos not in grid:
            break

        if grid[next_pos] == WALL:
            direction = next_direction(direction)
            continue

        current = next_pos

    return len(visited)


def part_2(data):
    result = 0
    guard, grid = data

    def walk(start):
        current = start
        direction = 'up'
        visited = set()
        while True:
            visited.add((current, direction))

            next_pos = next_position(current, direction)
            if next_pos not in grid:
                return None

            if grid[next_pos] == WALL:
                direction = next_direction(direction)
                continue

            if (next_pos, direction) in visited:
                return visited

            current = next_pos

    min_x = 0
    max_x = max([x[0] for x in data[1]])
    min_y = 0
    max_y = max([x[1] for x in data[1]])

    for i in range(min_x, max_x + 1):
        if (max_x - min_x >= 50):
            print(f"Processing line {i} out of {max_x}")
        for j in range(min_y, max_y + 1):
            if grid[(i, j)] != EMPTY and (i, j) != guard:
                continue

            grid[(i, j)] = WALL

            cycle = walk(guard)
            if cycle:
                result += 1
            grid[(i, j)] = EMPTY

    return result


def solve(filename):
    data = read(filename)

    print("part 1:")
    result = part_1(deepcopy(data))
    print(result)

    print("part 2:")
    result = part_2(deepcopy(data))
    print(result)


if __name__ == '__main__':
    # solve('test')
    solve('input')
