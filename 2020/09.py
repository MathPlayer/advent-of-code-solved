#!/usr/bin/env python

import sys

from itertools import combinations

def read(in_file):
    ''' Reads data for day 09. '''
    with open(in_file) as f:
        data = tuple(map(lambda x: int(x.strip()), f.readlines()))
    return data


def solve(in_file, preamble):
    ''' Solves day 09. '''
    data = read(in_file)
    print(in_file)

    # part 1 - data is small, O(n * preamble * preamble) works
    for (i, n) in enumerate(data):
        if i < preamble:
            continue
        if n not in [x+y for x, y in combinations(data[i - preamble:i], 2)]:
            break
    print(n)

    # part 2 - greedy ftw
    i, j = 0, 0
    total = data[0]
    while total != n:
        if total < n:
            j += 1
            total += data[j]
        elif total > n:
            total -= data[i]
            i += 1
    a = min(data[i:j+1])
    b = max(data[i:j+1])
    print(f"indices [{i}, {j}], min {a}, max {b}, answer {a+b}")


if __name__ == '__main__':
    solve('09test.in', 5)
    solve('09.in', 25)

    sys.exit(0)
