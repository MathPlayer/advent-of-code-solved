#!/usr/bin/python

import sys


if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = f.readline().strip()

    if not data:
        sys.exit(-1)

    print data.count("(") - data.count(")")

    floor = 0
    for (position, c) in enumerate(data):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            print position
            break
