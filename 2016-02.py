#!/usr/bin/python

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        move_list = map(str.strip, f.readlines())
        code = []
        for moves in move_list:
            position = [0, 0]
            for move in moves:
                if move == "L":
                    position[0] = max(-1, position[0] - 1)
                elif move == "R":
                    position[0] = min(1, position[0] + 1)
                if move == "U":
                    position[1] = max(-1, position[1] - 1)
                elif move == "D":
                    position[1] = min(1, position[1] + 1)
            code.append(5 + position[1] * 3 + position[0])
        print "".join(map(str, code))
    sys.exit(0)
