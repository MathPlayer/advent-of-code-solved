#!/usr/bin/python

from itertools import permutations


def solve(filename, sign):
    data = map(lambda x: x.strip().split(" = "),
               open(filename).readlines())
    cities = set()
    distances = {}
    for [ab, d] in data:
        [a, b] = ab.split(" to ")
        cities.add(a)
        cities.add(b)
        if a not in distances:
            distances[a] = {}
        if b not in distances:
            distances[b] = {}
        distances[a][b] = int(d)
        distances[b][a] = int(d)

    best = -1
    for perm in permutations(cities):
        count = 0
        for (a, b) in zip(perm, perm[1:]):
            count += distances[a][b]
        if count * sign < best * sign or best == -sign:
            best = count

    return best


print solve("09-test.in", 1)
print solve("09.in", 1)
print solve("09-test.in", -1)
print solve("09.in", -1)


