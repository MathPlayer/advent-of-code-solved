#!/usr/bin/env python3

from collections import deque


NEIGHBORS = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1)
}

PIPES = {
    '|': (NEIGHBORS['N'], NEIGHBORS['S']),
    '-': (NEIGHBORS['E'], NEIGHBORS['W']),
    'L': (NEIGHBORS['N'], NEIGHBORS['E']),
    'J': (NEIGHBORS['N'], NEIGHBORS['W']),
    '7': (NEIGHBORS['S'], NEIGHBORS['W']),
    'F': (NEIGHBORS['S'], NEIGHBORS['E']),
    'S': NEIGHBORS.values()
}
GROUND = '.'
ANIMAL = 'S'


def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        matrix = {}
        for row, line in enumerate(f):
            for col, char in enumerate(line):
                matrix[(row, col)] = char
                if char == ANIMAL:
                    start = (row, col)
    return matrix, start


def get_neighbors(pos, matrix):
    if matrix[pos] == GROUND:
        return
    for neighbor in PIPES[matrix[pos]]:
        yield (pos[0] + neighbor[0], pos[1] + neighbor[1])


def bfs(data):
    matrix, start = data
    visited = set()
    queue = deque()

    queue.append((start, 0))
    max_distance = 0
    while queue:
        current, distance = queue.popleft()
        max_distance = max(max_distance, distance)
        visited.add(current)

        for neighbor in get_neighbors(current, matrix):
            if current == start:
                if current not in get_neighbors(neighbor, matrix):
                    continue
            if neighbor not in matrix:
                continue
            if neighbor in visited:
                continue
            if matrix[neighbor] == GROUND:
                continue
            queue.append((neighbor, distance + 1))
    print(max_distance)


filename = 'test'
filename = 'test2'
filename = 'input'

data = read_matrix_from_file(filename)
bfs(data)
