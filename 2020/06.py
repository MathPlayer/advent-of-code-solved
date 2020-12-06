#!/usr/bin/env python

import sys


def read(in_file):
    ''' Reads data for day 06. '''
    with open(in_file) as f:
        data = tuple(x.strip() for x in f.readlines())
    return data


def solve(in_file):
    ''' Solves day 06. '''
    data = read(in_file)
    print(in_file)

    # part 1
    groups = []
    group = set()
    for line in data:
        if not line:
            groups.append(group)
            group = set()
        else:
            group |= set(line)
    groups.append(group)
    print(sum(map(len, groups)))

    # part 2
    groups = []
    group = set()
    first_in_group = True
    for line in data:
        if not line:
            groups.append(group)
            group = set()
            first_in_group = True
        elif first_in_group:
            # Add all first person's questions
            group |= set(line)
            first_in_group = False
        else:
            # Remove from group any questions not existing
            group &= set(line)
    groups.append(group)
    print(sum(map(len, groups)))


if __name__ == '__main__':
    solve('06test.in')
    solve('06.in')

    sys.exit(0)

