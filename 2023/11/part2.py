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


def get_expansion(matrix, row_count, col_count):
    expansion_rows = set()
    expansion_cols = set()
    for row in range(row_count):
        if all([matrix[(row, col)][0] == SPACE for col in range(col_count)]):
            expansion_rows.add(row)
    for col in range(col_count):
        if all([matrix[(row, col)][0] == SPACE for row in range(row_count)]):
            expansion_cols.add(col)

    return expansion_rows, expansion_cols


def get_distance(matrix, pos1, pos2, expansion_rows, expansion_cols, expansion_distance):
    row_dist = abs(pos1[0] - pos2[0])
    col_dist = abs(pos1[1] - pos2[1])

    for row in range(min(pos1[0], pos2[0]) + 1, max(pos1[0], pos2[0])):
        if row in expansion_rows:
            row_dist += expansion_distance - 1

    for col in range(min(pos1[1], pos2[1]) + 1, max(pos1[1], pos2[1])):
        if col in expansion_cols:
            col_dist += expansion_distance - 1

    return row_dist + col_dist


def solve(filename):

    matrix, row_count, col_count = read_matrix(filename)
    expansion_rows, expansion_cols = get_expansion(matrix, row_count, col_count)

    galaxies = {pos for pos, char in matrix.items() if char == GALAXY}
    result = 0
    for g1, g2 in product(galaxies, galaxies):
        if g1 != g2:
            distance = get_distance(matrix, g1, g2, expansion_rows, expansion_cols, 1000000)
            result += distance
    print(result // 2)


filename = 'test1'
filename = 'input'

solve(filename)
