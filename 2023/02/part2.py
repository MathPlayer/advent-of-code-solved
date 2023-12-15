#!/usr/bin/env python

from collections import defaultdict

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_game(line: str):
    i, data = line.strip().split(':')
    i = i.split(' ')[-1]
    i = int(i)
    data = data.split(';')
    cubes = defaultdict(int)
    for show in data:
        split = [x.strip() for x in show.split(',')]
        for n_cubes in split:
            v, color = n_cubes.split(' ')
            cubes[color] = max(int(v), cubes[color])
    return (i, cubes)


filename = 'input'
# filename = 'test'

data = open(filename).read()

power = 0
for line in data.splitlines():
    i, game = parse_game(line)
    result = 1
    for value in game.values():
        result *= value
    power += result
print(power)
