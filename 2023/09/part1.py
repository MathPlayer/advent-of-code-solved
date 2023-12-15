#!/usr/bin/env python3

from itertools import pairwise


# Read all lines from a file
def read_file(filename):
    with open(filename) as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]


def find_next_value(initial_line):

    def differences(numbers):
        return [b - a for a, b in pairwise(numbers)]

    lines = [initial_line]
    while any(x != 0 for x in lines[-1]):
        lines.append(differences(lines[-1]))

    next_value = sum(line[-1] for line in lines)
    return next_value


def solve(data):
    return sum(find_next_value(line) for line in data)


filename = 'input'
# filename = 'test'

data = read_file(filename)
print(solve(data))
