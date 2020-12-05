#!/usr/bin/env python

import sys


def read(in_file):
    ''' Reads data for day 05. '''
    with open(in_file) as f:
        data = tuple(x.strip() for x in f.readlines())
            for x in f.readlines())
    return data


def decode(seat):

    def change_up(pair):
        ''' Keeps the up part of the pair. '''
        return (pair[0], (pair[0] + pair[1]) // 2)

    def change_down(pair):
        ''' Keeps the down part of the pair. '''
        return ((pair[0] + pair[1]) // 2 + 1, pair[1])
    ''' Gives back the ID of a seat. '''

    row = (0, 127)
    col = (0, 7)

    for char in seat:
        if char == 'F':
            row = change_up(row)
        if char == 'B':
            row = change_down(row)
        if char == 'L':
            col = change_up(col)
        if char == 'R':
            col = change_down(col)
    return row[0] * 8 + col[0]


def solve(in_file):
    ''' Solves day 05. '''
    data = read(in_file)
    print(in_file)
    # Get IDs.
    ids = set(map(decode, data))
    # part 1
    print(max(ids))
    # part 2
    for i in range(min(ids), max(ids)):
        if i not in ids:
            print(i)
            return
    print("No seat found")  # For test one


if __name__ == '__main__':
    solve('05test.in')
    solve('05.in')

    sys.exit(0)
