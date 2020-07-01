#!/usr/bin/env python3
""" Solve day 10 of 2019. """

import sys


def read_asteroids(filename):
    """ Read asteroids from filename. """
    asteroids = set()
    with open(filename) as open_file:
        lines = list(map(str.strip, open_file.readlines()))
    for (y_coord, line) in enumerate(lines):
        for (x_coord, element) in enumerate(line):
            if element == '#':
                asteroids.add((x_coord, y_coord))

    return asteroids


def dist(x_1, y_1, x_2, y_2):
    """ Compute the distance. """
    return (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2


def slope(x_1, y_1, x_2, y_2):
    """ Compute the slope. Assume good values. """
    return float(y_1 - y_2) / (x_1 - x_2)


def solve(filename):
    """ Solve day 10 for the input data from filename. """
    asteroids = read_asteroids(filename)

    station = None
    best_count = -1
    for (x_1, y_1) in asteroids:
        slopes = set()
        for (x_2, y_2) in asteroids:
            if x_1 == x_2 and y_1 == y_2:
                continue
            if x_1 == x_2:
                new_slope = 'v'
                new_sign = '+' if y_1 < y_2 else '-'
            elif y_1 == y_2:
                new_slope = 0
                new_sign = '+' if x_1 < x_2 else '-'
            else:
                new_slope = float(y_1 - y_2) / (x_1 - x_2)
                new_sign = '+' if y_1 < y_2 else '-'
            slopes.add((new_sign, new_slope))

        if best_count < len(slopes):
            best_count = len(slopes)
            station = (x_1, y_1)
    print(best_count)

    asteroids.discard(station)
    discarded = []

    def check():
        """ Early return. """
        if len(discarded) >= 200:
            print(discarded[199][0] * 100 + discarded[199][1])
            sys.exit(0)

    while asteroids:
        slopes = {}
        x_1, y_1 = station
        for (x_2, y_2) in asteroids:
            if x_1 == x_2 and y_1 == y_2:
                continue
            if x_1 == x_2:
                new_slope = 'v'
                new_sign = '-' if y_1 < y_2 else '+'
            elif y_1 == y_2:
                new_slope = 0
                new_sign = '+' if x_1 < x_2 else '-'
            else:
                new_slope = slope(x_1, y_1, x_2, y_2)
                new_sign = '+' if y_1 < y_2 else '-'
            slopes[(x_2, y_2)] = (new_sign, new_slope)

        # + v
        values = [x for (x, (sign, value)) in slopes.items()
                  if x not in discarded and sign == '+' and value == 'v']
        if values:
            discard = min(values, key=lambda x: dist(station[0], station[1], x[0], x[1]))
            discarded.append(discard)
            asteroids.discard(discard)
            check()

        # + -
        # + h
        # + +
        values = [(value, x) for (x, (sign, value)) in slopes.items()
                  if x not in discarded and sign == '+' and value != 'v']
        values = sorted(values)
        while values:
            discard = values.pop(0)
            discarded.append(discard[1])
            asteroids.discard(discard)
            check()
            while values and values[0][0] == discard[0]:
                values.pop(0)

        # - v
        values = [x for (x, (sign, value)) in slopes.items()
                  if x not in discarded and sign == '-' and value == 'v']
        if values:
            discard = min(values, key=lambda x: dist(station[0], station[1], x[0], x[1]))
            del slopes[discard]
            discarded.append(discard)

        # - -
        # - h
        # - +
        values = [(value, x) for (x, (sign, value)) in slopes.items()
                  if x not in discarded and sign == '-' and value != 'v']
        values = sorted(values)
        while values:
            discard = values.pop(0)
            discarded.append(discard[1])
            asteroids.discard(discard)
            check()
            while values and values[0][0] == discard[0]:
                values.pop(0)


if __name__ == '__main__':
    # solve("10-example.in")
    solve("10.in")
