#!/usr/bin/env python3

from itertools import product

SPACE = '.'
GALAXY = '#'


def read_matrix(filename):
    matrix = {}
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
        row_count = len(data)
        col_count = len(data[0])
        for row, line in enumerate(data):
            for col, char in enumerate(line):
                matrix[(row, col)] = char
    return matrix, row_count, col_count


def print_matrix(matrix, row_count, col_count):
    for row in range(row_count):
        for col in range(col_count):
            print(matrix[(row, col)], end='')
        print()


def get_neighbors(matrix, pos):
    for row in range(pos[0] - 1, pos[0] + 2):
        for col in range(pos[1] - 1, pos[1] + 2):
            if (row, col) != pos and (row, col) in matrix:
                yield (row, col)


def expand_matrix(matrix, row_count, col_count):
    def get_new_matrix():
        new_matrix = {}
        row_values = sorted(set([row for row, _ in matrix]))
        col_values = sorted(set([col for _, col in matrix]))
        for row, row_value in enumerate(row_values):
            for col, col_value in enumerate(col_values):
                new_matrix[(row, col)] = matrix[(row_value, col_value)]
        return new_matrix

    row_changes = 0
    for row in range(row_count):
        if all([matrix[(row, col)][0] == SPACE for col in range(col_count)]):
            row_changes += 1
            for col in range(col_count):
                matrix[(row + 0.5, col)] = SPACE
    matrix = get_new_matrix()
    row_count += row_changes

    col_changes = 0
    for col in range(col_count):
        if all([matrix[(row, col)][0] == SPACE for row in range(row_count)]):
            col_changes += 1
            for row in range(row_count):
                matrix[(row, col + 0.5)] = SPACE
    matrix = get_new_matrix()
    col_count += col_changes

    return matrix, row_count, col_count


def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def solve(filename):

    matrix, row_count, col_count = read_matrix(filename)
    matrix, row_count, col_count = expand_matrix(matrix, row_count, col_count)

    galaxies = {pos for pos, char in matrix.items() if char == GALAXY}
    result = 0
    for g1, g2 in product(galaxies, galaxies):
        if g1 != g2:
            result += get_distance(g1, g2)
    print(result // 2)


filename = 'test1'
filename = 'input'

solve(filename)
