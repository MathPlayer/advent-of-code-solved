#!/usr/bin/env python

import sys

TREE = '#'
EMPTY = '.'


def read(in_file):
    ''' Reads data for day 03. '''
    with open(in_file) as f:
        data = tuple(x.strip() for x in f.readlines())
    return data


def solve(in_file, slope):
    ''' Solves day 03. '''
    data = read(in_file)

    pos = [0, 0]
    w = len(data[0])

    count = 0
    while pos[1] < len(data):
        if data[pos[1]][pos[0]] == TREE:
            count += 1
        pos = [(pos[0] + slope[0]) % w, pos[1] + slope[1]]
    return count


if __name__ == '__main__':
    print("part 1")
    print(solve('03test.in', [3, 1]))
    print(solve('03.in', [3, 1]))

    print("part 2")
    res_test, res = 1, 1
    for slope in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        res_test *= solve('03test.in', slope)
        res *= solve('03.in', slope)
    print(res_test)
    print(res)

    sys.exit(0)