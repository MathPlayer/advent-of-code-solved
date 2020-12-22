#!/usr/bin/env python

import sys

from collections import deque

def read(in_file):
    ''' Reads data for day 22. '''
    data = {1: deque(), 2: deque()}
    with open(in_file) as f:
        for line in map(lambda x: x.strip(), f.readlines()):
            if not line:
                continue
            if 'Player' in line:
                player = int(line[-2])
                continue
            data[player].append(int(line))
    return data[1], data[2]


def update(p1, p2, c1, c2, cond):
    ''' Adds c1 and c2 to p1 if cond else to p2. '''
    if cond:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)


def combat(p1, p2):
    ''' Returns the winner of a normal game between p1 and p2. '''
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        update(p1, p2, c1, c2, c1 > c2)
    return p1 if p1 else p2


def recursive_combat(p1, p2):
    ''' Returns the pair (<1 or 2>, px) for the winner of a recursive game between p1 and p2. '''
    states = set()
    while p1 and p2:
        state = (tuple(p1), tuple(p2))
        if state in states:
            return (1, p1)
        states.add(state)
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 <= len(p1) and c2 <= len(p2):
            i, _ = recursive_combat(deque(list(p1)[:c1]), deque(list(p2)[:c2]))
            update(p1, p2, c1, c2, i == 1)
        else:
            update(p1, p2, c1, c2, c1 > c2)
    return (1, p1) if p1 else (2, p2)


def score(winner):
    ''' Prints the winner's score. '''
    print(sum(map(lambda x: (x[0] + 1) * x[1], enumerate(reversed(winner)))))


def solve(in_file):
    ''' Solves day 22. '''
    p1, p2 = read(in_file)
    print(f"--- {in_file}")

    score(combat(p1.copy(), p2.copy()))
    score(recursive_combat(p1.copy(), p2.copy())[1])


if __name__ == '__main__':
    solve('22test.in')
    solve('22.in')

    sys.exit(0)
