#!/usr/bin/python

import sys


if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = map(lambda x: x.strip().split(), f.readlines())

    if not data:
        sys.exit(-1)

    lights = [[0] * 1000 for _ in xrange(1000)]
    for order in data:
        if order[0] == "toggle":
            start = map(int, order[1].split(","))
            stop = map(int, order[-1].split(","))
            for i in xrange(start[0], stop[0] + 1):
                for j in xrange(start[1], stop[1] + 1):
                    lights[i][j] = 1 - lights[i][j]
        elif order[0] == "turn":
            value = 1 if order[1] == "on" else 0
            start = map(int, order[2].split(","))
            stop = map(int, order[-1].split(","))
            for i in xrange(start[0], stop[0] + 1):
                for j in xrange(start[1], stop[1] + 1):
                    lights[i][j] = value
    print sum(map(sum, lights))

    lights = [[0] * 1000 for _ in xrange(1000)]
    for order in data:
        if order[0] == "toggle":
            start = map(int, order[1].split(","))
            stop = map(int, order[-1].split(","))
            for i in xrange(start[0], stop[0] + 1):
                for j in xrange(start[1], stop[1] + 1):
                    lights[i][j] += 2
        elif order[0] == "turn":
            value = 1 if order[1] == "on" else -1
            start = map(int, order[2].split(","))
            stop = map(int, order[-1].split(","))
            for i in xrange(start[0], stop[0] + 1):
                for j in xrange(start[1], stop[1] + 1):
                    lights[i][j] = max(0, lights[i][j] + value)
    print sum(map(sum, lights))
