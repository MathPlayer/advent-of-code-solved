#!/usr/bin/env python3
""" Solve day 06 of 2019. """

from collections import deque


def read_orbits(name):
    """ Reads orbits from the named file. """
    orbits = {}
    with open(name) as in_file:
        raw_orbits = [(x, y) for (x, y) in map(lambda x: x.strip().split(")"), in_file.readlines())]

    for (x, y) in raw_orbits:
        if x not in orbits:
            orbits[x] = set()
        orbits[x].add(y)
    return orbits


def count_orbits(name):
    """ Solves part 1. """
    orbits = read_orbits(name)

    queue = deque([])

    queue.append(('COM', 0))
    count = 0
    while queue:
        (top, layer) = queue.popleft()
        if top not in orbits:
            continue
        for orbiter in orbits[top]:
            queue.append((orbiter, layer + 1))
            count += layer + 1
    print(count)


def find_parents(orbits, node):
    """ Obtains the parent list for a given node. """

    parent = node
    parents = []
    while parent != 'COM':
        for (key, values) in orbits.items():
            if parent in values:
                parents.append(key)
                parent = key
                break

    return parents


def print_orbit_transfer_count(name):
    """ Solves part 2. """
    orbits = read_orbits(name)
    parents_1 = find_parents(orbits, 'YOU')
    parents_2 = find_parents(orbits, 'SAN')

    # Look for the first common ancestor.
    for i in range(len(parents_1)):
        if parents_1[i] in parents_2:
            j = parents_2.index(parents_1[i])
            print(i + j)
            break


if __name__ == "__main__":
    count_orbits("06-example.in")
    count_orbits("06.in")

    print_orbit_transfer_count("06-example-2.in")
    print_orbit_transfer_count("06.in")


