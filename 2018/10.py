#!/usr/bin/env python3

import pdb
import pprint


def read(filename):
    with open(filename) as f_in:
        raw_data = f_in.readlines()
        data = []
        for line in raw_data:
            s = line.split("<")
            coords = list(map(int, s[1].split(">")[0].split(", ")))
            velocities = list(map(int, s[2].split(">")[0].split(", ")))
            data.append([coords, velocities])
    return data


def update(data):
    new_data = []
    for (coords, velocities) in data:
        new_data.append([list(map(sum, zip(coords, velocities))), velocities])
    return new_data


def print_map(data, min_x, min_y, max_x, max_y):
    pretty_map = []
    for _ in range(max_y - min_y + 2):
        pretty_map.append(['.'] * (max_x - min_x + 1))

    for (coords, _) in data:
        pretty_map[coords[1] - min_y][coords[0] - min_x] = '#'

    print("\n".join(map(lambda x: "".join(x), pretty_map)))
    print("")


def get_edges(data):
    min_x, min_y, max_x, max_y = None, None, None, None
    for (coords, _) in data:
        if not min_x:
            min_x = coords[0]
            max_x = coords[0]
            min_y = coords[1]
            max_y = coords[1]
        else:
            min_x = min(min_x, coords[0])
            min_y = min(min_y, coords[1])
            max_x = max(max_x, coords[0])
            max_y = max(max_y, coords[1])
    return (min_x, min_y, max_x, max_y)


data = read("10.in")
(best_min_x, best_min_y, best_max_x, best_max_y) = get_edges(data)
(min_x, min_y, max_x, max_y) = get_edges(data)
best_data = data
best = 0
for i in range(20000):
    data = update(data)
    if i % 1000 == 0:
        print("Debug: {}".format(i))
    fx, fy, tx, ty = get_edges(data)
    if ty - fy <= best_max_y - best_min_y:
        best_data = data
        best_min_x, best_min_y, best_max_x, best_max_y = fx, fy, tx, ty
        best = i + 1
print(best)
print_map(best_data, best_min_x, best_min_y, best_max_x, best_max_y)
