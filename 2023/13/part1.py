#!/usr/bin/env python3


def read_patterns_from_file(filename):
    patterns = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        pattern = {}
        row = 0
        max_col = -1

        for line in map(str.strip, lines):
            if not line:
                patterns.append((pattern.copy(), row, max_col))
                pattern = {}
                row = 0
                max_col = -1
                continue

            for col, char in enumerate(line):
                pattern[(row, col)] = char

            row += 1
            max_col = max(max_col, len(line))

    patterns.append((pattern, row, max_col))
    return patterns


def print2d(pattern, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if (row, col) in pattern:
                print(pattern[(row, col)], end='')
        print()
    print("---")


def find_reflection_on_col(pattern, rows, cols):
    for symmetry in range(cols - 1):
        mirror = True
        for col in range(cols):
            col_left = symmetry - col
            col_right = symmetry + col + 1
            if col_left < 0 or col_right >= cols:
                break
            col_mirror = True
            for row in range(rows):
                if pattern[(row, col_left)] != pattern[(row, col_right)]:
                    col_mirror = False
                    break
            if not col_mirror:
                mirror = False
                break
        if mirror:
            return symmetry + 1
    return None


def find_reflection_on_row(pattern, rows, cols):
    for symmetry in range(rows - 1):
        mirror = True
        for row in range(rows):
            row_top = symmetry - row
            row_bottom = symmetry + row + 1
            if row_top < 0 or row_bottom >= rows:
                break
            row_mirror = True
            for col in range(cols):
                if pattern[(row_top, col)] != pattern[(row_bottom, col)]:
                    row_mirror = False
                    break
            if not row_mirror:
                mirror = False
                break
        if mirror:
            return symmetry + 1
    return None


def solve(filename):
    patterns = read_patterns_from_file(filename)
    result = 0
    for pattern, rows, cols in patterns:
        symmetry = find_reflection_on_col(pattern, rows, cols)
        if symmetry:
            result += symmetry
            continue
        symmetry = find_reflection_on_row(pattern, rows, cols)
        if symmetry:
            result += symmetry * 100
            continue
        raise Exception("No symmetry found")
    print(result)


filename = 'test'
filename = 'input'

solve(filename)
