#!/usr/bin/env python3
""" Solves day 03 of 2019. """

import sys


def read_data(filename):
    """ Reads data from filename. """
    with open(filename) as opened:
        lines = [x.strip().split(",") for x in opened.readlines()]
    coords = []
    for line in lines:
        coords.append([[y[0], int(y[1:])] for y in line])

    return coords


def get_grid(coords):
    """ Returns a dict with coordinates touched by the first wire and their count steps. """
    updates = {
        "L": [-1, 0],
        "R": [1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    grid = {}
    position = (0, 0)
    count = 0
    for [direction, distance] in coords:
        for _ in range(distance):
            position = (position[0] + updates[direction][0], position[1] + updates[direction][1])
            count += 1
            grid[position] = count

    return grid


def main():
    """ Entrypoint for calling the script from CLI. """
    wire_coords = read_data("03.in")
    grid_1 = get_grid(wire_coords[0])
    grid_2 = get_grid(wire_coords[1])

    # Min Manhattan distance for common coords.
    print(min(list(map(lambda x: abs(x[0]) + abs(x[1]), grid_1.keys() & grid_2.keys()))))

    # Min distance as sum of counts for common coords.
    print(min(list(map(lambda x: grid_1[x] + grid_2[x], grid_1.keys() & grid_2.keys()))))

    return 0


if __name__ == "__main__":
    sys.exit(main())
