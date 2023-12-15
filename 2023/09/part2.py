#!/usr/bin/env python3

from itertools import pairwise


def read_file(filename):
    with open(filename) as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]


def find_previous_value(initial_line):

    def differences(numbers):
        return [b - a for a, b in pairwise(numbers)]

    lines = [initial_line]
    while any(x != 0 for x in lines[-1]):
        lines.append(differences(lines[-1]))

    previous_value = 0

    print(initial_line)
    for i in range(len(lines) - 1, -1, -1):
        previous_value = lines[i][0] - previous_value
        print(previous_value)

    print("returning", previous_value)
    return previous_value


def solve(data):
    return sum(find_previous_value(line) for line in data)


filename = 'input'
# filename = 'test'

data = read_file(filename)
print(solve(data))
