#!/usr/bin/python

import sys


if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = f.readline().strip()

    if not data:
        sys.exit(-1)

    commands = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}

    position = (0, 0)
    visited = set()
    visited.add(position)

    for c in data:
        position = tuple(map(sum, zip(position, commands[c])))
        visited.add(position)

    print len(visited)

    position = (0, 0)
    visited = set()
    visited.add(position)

    for c in data[::2]:
        position = tuple(map(sum, zip(position, commands[c])))
        visited.add(position)

    position = (0, 0)
    for c in data[1::2]:
        position = tuple(map(sum, zip(position, commands[c])))
        visited.add(position)

    print len(visited)
