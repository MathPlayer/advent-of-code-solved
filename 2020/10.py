#!/usr/bin/env python

import sys

from itertools import combinations

def read(in_file):
    ''' Reads data for day 09. '''
    with open(in_file) as f:
        data = tuple(map(lambda x: int(x.strip()), f.readlines()))
    return data


def solve(in_file,):
    ''' Solves day 10. '''
    print(in_file)
    data = read(in_file)
    elements = sorted(data)
    elements = [0] + elements + [elements[-1] + 3]

    # part 1
    diff1 = 0
    diff3 = 0
    for i in range(len(elements) - 1):
        if elements[i + 1] - elements[i] == 1:
            diff1 += 1
        elif elements[i + 1] - elements[i] == 3:
            diff3 += 1
    print(diff1, diff3, diff1 * diff3)

    # part 2
    count = [0] * len(elements)
    count[0] = 1
    for i, x in enumerate(elements):
        j = i - 1
        while j >= 0:
            if x - elements[j] <= 3:
                count[i] += count[j]
            else:
                break
            j -= 1
    print(count[-1])


if __name__ == '__main__':
    solve('10test.in')
    solve('10test2.in')
    solve('10.in')

    sys.exit(0)
