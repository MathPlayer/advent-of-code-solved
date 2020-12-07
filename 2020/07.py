#!/usr/bin/env python

import sys


def read(in_file):
    ''' Reads data for day 07. '''
    with open(in_file) as f:
        data = tuple(
            x.strip('.\n').replace(' bags', '').replace(' bag', '').split(' contain ')
            for x in f.readlines()
        )

    return {
        name: {} if content == 'no other' else {
            subbags[1]: int(subbags[0])
            for subbags in map(lambda x: x.split(' ', 1), content.split(', '))
        }
        for name, content in data
    }


def solve(in_file):
    ''' Solves day 07. '''
    bags = read(in_file)
    print(in_file)

    start = 'shiny gold'

    # Part 1: find all anchestors of start
    anchestors = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        anchestors.add(current)
        queue.extend(bag for bag, subbags in bags.items() if current in subbags)
    print(len(anchestors) - 1)  # without start

    # Part 2: count all bags inside start and its descendants
    total = 0
    queue = [(1, start)]
    while queue:
        factor, current = queue.pop(0)
        total += factor * sum(bags[current].values())
        queue.extend((factor * count, name) for name, count in bags[current].items())
    print(total)


if __name__ == '__main__':
    solve('07test.in')
    solve('07test2.in')
    solve('07.in')

    sys.exit(0)
