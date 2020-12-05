#!/usr/bin/env python

import sys

TRANSLATION = str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'})


def read(in_file):
    ''' Reads data for day 05. '''
    with open(in_file) as f:
        data = tuple(x.strip() for x in f.readlines())
    return data


def decode(seat):
    ''' Gives back the ID of a seat. '''
    seat = seat.translate(TRANSLATION)
    row = int(seat[:7], 2)
    col = int(seat[7:], 2)
    return row * 8 + col


def solve(in_file):
    ''' Solves day 05. '''
    data = read(in_file)
    print(in_file)
    ids = set(map(decode, data))
    # part 1
    print(max(ids))
    # part 2
    for i in range(min(ids), max(ids)):
        if i not in ids:
            print(i)
            return


if __name__ == '__main__':
    solve('05test.in')
    solve('05.in')

    sys.exit(0)

