#!/usr/bin/env python

import re
import sys

from math import prod

CONDITION = re.compile('([^:]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')

def read(in_file):
    ''' Reads data for day 15. '''
    conditions = {}
    ticket = []
    nearby = set()
    with open(in_file) as f:
        for line in map(lambda x: x.strip(), f.readlines()):
            if not line:
                continue
            if line == 'your ticket:':
                state = 'ticket'
                continue
            elif line == 'nearby tickets:':
                state = 'nearby'
                continue

            if CONDITION.match(line):
                groups = CONDITION.match(line).groups()
                conditions[groups[0]] = ((int(groups[1]), int(groups[2])), (int(groups[3]), int(groups[4])))
            elif state == 'ticket':
                ticket = tuple(int(x) for x in line.split(','))
            elif state == 'nearby':
                nearby.add(tuple(int(x) for x in line.split(',')))

    return conditions, ticket, nearby


def solve_1(data):
    ''' Returns the invalid sum and the tickets which are invalid. '''
    conditions, _, nearby = data
    invalid_sum = 0
    invalid_tickets = set()
    for ticket in nearby:
        for number in ticket:
            valid = False
            for (a, b), (x, y) in conditions.values():
                if (a <= number <= b) or (x <= number <= y):
                    valid = True
                    break
            if not valid:
                invalid_sum += number
                invalid_tickets.add(ticket)
    return invalid_sum, invalid_tickets


def solve_2(data, invalid_tickets):
    ''' Determines the name order on the ticket and computes the product of the numbers on our ticket for the fields
    starting their name with 'departure'. '''
    # Determine matches for all indices.
    conditions, our_ticket, nearby = data
    matches = [set(conditions.keys()) for _ in conditions]
    for ticket in nearby - invalid_tickets:
        for index, number in enumerate(ticket):
            for name, ((a, b), (x, y)) in conditions.items():
                if not (a <= number <= b) and not (x <= number <= y):
                    matches[index].remove(name)

    # Some fields have multiple matched fields, reduce them.
    while any(len(match) > 1 for match in matches):
        unique_matches = set.union(*[match for match in matches if len(match) == 1])
        matches = [match - unique_matches if len(match) > 1 else match for match in matches]
    matches = [list(match)[0] for match in matches]

    # Determine the product of numbers on our ticket for the fields saring their name with 'departure'.
    print(prod(v for (match, v) in zip(matches, our_ticket) if match.startswith('departure')))


def solve(in_file):
    ''' Solves day 16. '''
    data = read(in_file)
    print(f"--- {in_file}")
    invalid, to_drop = solve_1(data)
    print(invalid)
    solve_2(data, to_drop)


if __name__ == '__main__':
    solve('16test.in')
    solve('16.in')

    sys.exit(0)
