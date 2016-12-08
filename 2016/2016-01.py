#!/usr/bin/python

import sys


if __name__ == "__main__":
    signs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    index = 0
    position = [0, 0]
    visited = []
    visited_twice = None
    with open(sys.argv[1]) as f:
        instructions = f.readline().strip().split(", ")
        for instruction in instructions:
            if instruction[0] == "L":
                index = (index + 1) % 4
            elif instruction[0] == "R":
                index = (index - 1) % 4
            else:
                continue
            steps = int(instruction[1:])

            visiting = position[:]
            position[0] += steps * signs[index][0]
            position[1] += steps * signs[index][1]

            if visited_twice:
                continue
            for _ in xrange(steps):
                visiting[0] += signs[index][0]
                visiting[1] += signs[index][1]
                if not visited or visiting not in visited:
                    visited.append(visiting[:])
                else:
                    visited_twice = visiting[:]
                    break


        print abs(position[0]) + abs(position[1])
        print abs(visited_twice[0]) + abs(visited_twice[1])
    sys.exit(0)
