#!/usr/bin/python

import sys
import itertools


def is_triangle(sides):
    for side in sides:
        other_sides = sum(sides) - side
        if side >= other_sides:
            return False
    return True

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        values = map(lambda x: [int(y) for y in x.strip().split()],
                     f.readlines())

        print sum(map(is_triangle, values))

        i = iter(values)
        print sum(map(is_triangle,
                      reduce(lambda acc, y: acc + y,
                             [zip(*x) for x in itertools.izip(i, i, i)], [])))

    sys.exit(0)
