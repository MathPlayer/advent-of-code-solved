#!/usr/bin/env python3

from collections import deque
from functools import lru_cache

GROUND = '.'
ANIMAL = 'S'
LOOP = '*'
ANSWER = '#'
FLOOD = ' '

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
CONNECTIONS = {
    '|': set((DIRECTIONS[x] for x in (U, D))),
    '-': set((DIRECTIONS[x] for x in (L, R))),
    'L': set((DIRECTIONS[x] for x in (U, R))),
    'J': set((DIRECTIONS[x] for x in (U, L))),
    '7': set((DIRECTIONS[x] for x in (D, L))),
    'F': set((DIRECTIONS[x] for x in (D, R))),
    GROUND: DIRECTIONS.values()
}


def read_data(filename):
    data = {}
    with open(filename) as f:
        for row, line in enumerate(f):
            for col, value in enumerate(line.strip()):
                data[(row, col)] = value
                if value == ANIMAL:
                    start_pos = (row, col)
    return data, start_pos


@lru_cache
def get_next(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def get_neighbors(pos, data, flood=False):
    if not flood:
        directions = CONNECTIONS.get(data[pos], DIRECTIONS.values())
    else:
        directions = DIRECTIONS.values()
    for neigh in (get_next(pos, d) for d in directions):
        if neigh not in data:
            continue
        yield neigh


def determine_start_type(start, data):
    directions = ''
    for neighbor in get_neighbors(start, data):
        if neighbor not in data or start not in get_neighbors(neighbor, data):
            continue
        if data[neighbor] == GROUND:
            continue

        if neighbor[0] < start[0]:
            directions += U
        elif neighbor[0] > start[0]:
            directions += D
        elif neighbor[1] < start[1]:
            directions += L
        elif neighbor[1] > start[1]:
            directions += R

    if U in directions and D in directions:
        return '|'
    if L in directions and R in directions:
        return '-'
    if U in directions and R in directions:
        return 'L'
    if U in directions and L in directions:
        return 'J'
    if D in directions and L in directions:
        return '7'
    if D in directions and R in directions:
        return 'F'

    raise Exception('Unknown start type')


def double_up(data, start):
    # Make space between walls for flodding.
    mapping = {
        '.': ['..', '..'],
        '-': ['--', '..'],
        '|': ['|.', '|.'],
        'L': ['L-', '..'],
        'J': ['J.', '..'],
        'F': ['F-', '|.'],
        '7': ['7.', '|.']
    }
    new_data = {}
    for (row, col), value in data.items():
        for r in range(2):
            for c in range(2):
                new_data[(row * 2 + r, col * 2 + c)] = mapping[value][r][c]
    return new_data, (start[0] * 2, start[1] * 2)


def bfs(data, start, flood=False):
    visited = set()
    queue = deque()

    queue.append(start)
    while queue:
        node = queue.popleft()
        visited.add(node)
        for next in get_neighbors(node, data, flood):
            if next not in data:
                continue
            if next in visited:
                continue
            if not flood and data[next] == GROUND:
                continue
            if flood and data[next] == LOOP:
                continue
            if flood:
                visited.add(next)

            queue.append(next)

    return visited


def pad_matrix(data, pad_value):
    min_row = min(pos[0] for pos in data)
    max_row = max(pos[0] for pos in data)
    min_col = min(pos[1] for pos in data)
    max_col = max(pos[1] for pos in data)

    for row in range(min_row - 1, max_row + 2):
        data[(row, min_col - 1)] = pad_value
        data[(row, max_col + 1)] = pad_value
    for col in range(min_col - 1, max_col + 2):
        data[(min_row - 1, col)] = pad_value
        data[(max_row + 1, col)] = pad_value


def print_matrix(data):
    min_row = min(pos[0] for pos in data)
    max_row = max(pos[0] for pos in data)
    min_col = min(pos[1] for pos in data)
    max_col = max(pos[1] for pos in data)

    for row in range(min_row, max_row + 1):
        line = f"{row:3d} "
        for col in range(min_col, max_col + 1):
            line += data[(row, col)]
        print(line)
    print()


def solve(data, start):
    data[start] = determine_start_type(start, data)

    data, start = double_up(data, start)
    pad_matrix(data, GROUND)

    pipe_loop = bfs(data, start)
    data.update({pos: LOOP for pos in pipe_loop})

    flood = bfs(data, (-1, -1), flood=True)
    data.update({pos: FLOOD for pos in flood})

    inside = set()
    for pos, value in data.items():
        if pos[0] % 2 or pos[1] % 2:
            continue
        if value != LOOP and value != FLOOD:
            inside.add(pos)
    data.update({pos: ANSWER for pos in inside})

    print(len(inside))


filename = 'test'
filename = 'test2'
filename = 'test3'
filename = 'test4'
filename = 'test5'
filename = 'input'

data, start_pos = read_data(filename)
solve(data, start_pos)

print("DONE")
