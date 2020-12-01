#!/usr/bin/env python

import sys

from itertools import combinations
from math import prod

def read(in_file):
    with open(in_file) as f:
        data = [int(x.strip()) for x in f.readlines()]
    return data

def solve(in_file, count):
    ''' Solve day 01. '''
    ints = read(in_file)
    for combo in combinations(ints, count):
        if sum(combo) == 2020:
            print(f"{in_file}, {count} -> {prod(combo)}")
            return

if __name__ == '__main__':
    solve('01test.in', 2)
    solve('01.in', 2)

    solve('01test.in', 3)
    solve('01.in', 3)

    sys.exit(0)