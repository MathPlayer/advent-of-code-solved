#!/usr/bin/python

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        move_list = map(str.strip, f.readlines())
        code1 = []
        code2 = []
        keypad = [["0","0","1","0","0"],
                  ["0","2","3","4","0"],
                  ["5","6","7","8","9"],
                  ["0","A","B","C","0"],
                  ["0","0","D","0","0"]]
        position1 = [0, 0]
        position2 = [-2, 0]
        for moves in move_list:
            for move in moves:
                if move == "L":
                    position1[0] = max(-1, position1[0] - 1)
                    position2[0] = max(-2 + abs(position2[1]), position2[0] - 1)
                elif move == "R":
                    position1[0] = min(1, position1[0] + 1)
                    position2[0] = min(2 - abs(position2[1]), position2[0] + 1)
                if move == "U":
                    position1[1] = max(-1, position1[1] - 1)
                    position2[1] = max(-2 + abs(position2[0]), position2[1] - 1)
                elif move == "D":
                    position1[1] = min(1, position1[1] + 1)
                    position2[1] = min(2 - abs(position2[0]), position2[1] + 1)
            code1.append(5 + position1[1] * 3 + position1[0])
            code2.append(keypad[2 + position2[1]][2 + position2[0]])

        print "".join(map(str, code1))
        print "".join(code2)
    sys.exit(0)
