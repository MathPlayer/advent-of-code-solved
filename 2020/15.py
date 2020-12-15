#!/usr/bin/env python

import re
import sys


def read(in_file):
    ''' Reads data for day 15. '''
    data = []
    with open(in_file) as f:
        data = list(map(lambda x: [int(a) for a in x.strip().split(',')], f.readlines()))
    return data[0]


def do_turns(data, max_turn):
    ''' Plays the elves' memory game. '''
    turns = {}
    for (i, d) in enumerate(data):
        turns[d] = i + 1  # Starting with turn 1

    current = 0
    for turn in range(len(data) + 1, max_turn + 1):
        if not turn % 5000000:
            print(f"On turn {turn} say {current}")
        if turn == max_turn:
            print(f"On last turn {turn} say {current}")
        if current in turns:
            new = turn - turns[current]
        else:
            new = 0
        turns[current] = turn
        current = new


def solve(in_file, max_turns):
    ''' Solves day 14. '''
    data = read(in_file)
    print(f"--- {in_file} - {max_turns}")
    do_turns(data, max_turns)


if __name__ == '__main__':
    solve('15test.in', 10)
    solve('15test.in', 2020)
    # Part 1
    solve('15.in', 2020)
    # Part 2
    solve('15.in', 30000000)

    sys.exit(0)
