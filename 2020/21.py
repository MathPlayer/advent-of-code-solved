#!/usr/bin/env python

import sys

def read(in_file):
    ''' Reads data for day 21. '''
    data = []
    with open(in_file) as f:
        for i, a in map(lambda x: x.replace(',', '').replace(')', '').split('(contains'), f.readlines()):
            data.append((set(i.split()), set(a.split())))
    return data


def solve(in_file):
    ''' Solves day 21. '''
    rules = read(in_file)
    print(f"--- {in_file}")

    # Get sets of all alergens and all ingredients.
    alergens, ingredients = set(), set()
    for i, a in rules:
        alergens.update(a)
        ingredients.update(i)

    # Find all (alergen, ingredient) associations.
    found = {}
    while len(found) < len(alergens):
        # Determine possible fixed ingredients.
        possible = {a: ingredients.copy() for a in alergens}
        for r_i, r_a in rules:
            for a in r_a:
                possible[a] = possible[a].intersection(r_i)
        # Get from possible the sure ones.
        found.update({a: list(s)[0] for a, s in possible.items() if len(s) == 1})
        # Update the rules with the new found items.
        rules = [
            (r_i.difference(found.values()), r_a.difference(found.keys()))
            for r_i, r_a in rules
        ]

    # Part 1: current rules contain all occurences of ingredients without the fixed ones.
    print(sum(map(lambda x: len(x[0]) if len(x[1]) == 0 else 0, rules)))

    # Part 2.
    print(','.join(found[s_a] for s_a in sorted(found)))


if __name__ == '__main__':
    solve('21test.in')
    solve('21.in')

    sys.exit(0)
