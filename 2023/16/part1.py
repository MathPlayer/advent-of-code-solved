#!/usr/bin/env python3

from collections import deque

EMPTY = '.'
MIRROR_PRINCIPAL = '/'
MIRROR_SECONDARY = '\\'
SPLIT_VERTICAL = '|'
SPLIT_HORIZONTAL = '-'
ENERGIZED = '#'

U = 'up'
D = 'down'
L = 'left'
R = 'right'
DIRECTIONS = {
    U: (-1, 0),
    D: (1, 0),
    L: (0, -1),
    R: (0, 1)
}
REFLECTIONS = {
    MIRROR_PRINCIPAL: {U: R, D: L, L: D, R: U},
    MIRROR_SECONDARY: {U: L, D: R, L: U, R: D}
}
SPLITTERS = {
    SPLIT_VERTICAL: {U: [U], D: [D], L: [U, D], R: [U, D]},
    SPLIT_HORIZONTAL: {U: [L, R], D: [L, R], L: [L], R: [R]}
}


def read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def process_lines(lines):
    result = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line.strip()):
            result[(row, col)] = char
    return result, len(lines), len(lines[0].strip())


def print2d(grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            print(grid[(row, col)], end='')
        print()
    print('---')


def energize(grid, rows, cols, start, direction):
    visited = set()
    queue = deque()
    queue.append((start, direction))
    while queue:
        current, direction = queue.pop()
        if current not in grid:
            continue

        if (current, direction) in visited:
            continue

        field = grid[current]
        visited.add((current, direction))

        if field == EMPTY:
            next = (current[0] + DIRECTIONS[direction][0], current[1] + DIRECTIONS[direction][1])
            queue.append((next, direction))

        if field in [MIRROR_PRINCIPAL, MIRROR_SECONDARY]:
            next = (current[0] + DIRECTIONS[REFLECTIONS[field][direction]][0],
                    current[1] + DIRECTIONS[REFLECTIONS[field][direction]][1])
            queue.append((next, REFLECTIONS[field][direction]))

        if field in [SPLIT_HORIZONTAL, SPLIT_VERTICAL]:
            for next_direction in SPLITTERS[field][direction]:
                next = (current[0] + DIRECTIONS[next_direction][0], current[1] + DIRECTIONS[next_direction][1])
                queue.append((next, next_direction))

    return visited


def solve(filename):
    grid, rows, cols = process_lines(read_lines(filename))
    print2d(grid, rows, cols)

    energized = energize(grid, rows, cols, (0, 0), R)
    for field, _ in energized:
        grid[field] = ENERGIZED
    print2d(grid, rows, cols)
    unique = {e for e, _ in energized}
    print(len(unique))


filename = 'test'
# filename = 'input'
solve(filename)
print("Done")
