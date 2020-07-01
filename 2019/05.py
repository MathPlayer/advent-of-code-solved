#!/usr/bin/env python3
""" Solving day 05 of 2019. """

import sys


def read(filename):
    """ Reads input data. """
    with open(filename) as input_file:
        file_data = [int(x) for x in input_file.read().strip().split(",")]

    return file_data


def solve(filename, input_value):
    """ Solves the problem with input read from filename. """
    ints = read(filename)
    # print("DEBUG len", len(ints))

    i = 0
    while True:
        # print("DEBUG index", i, "next-ish ops", ints[i:i+5])
        opcode = ints[i] % 100
        mode_1 = ints[i] // 100 % 10
        mode_2 = ints[i] // 1000 % 10
        # mode_3 = ints[i] // 10000
        # parameter_mode 0 - position, 1 - value
        if opcode == 99:
            break
        elif opcode == 1:
            # pos3 = pos1 + pos2
            p_1 = ints[ints[i + 1]] if mode_1 == 0 else ints[i + 1]
            p_2 = ints[ints[i + 2]] if mode_2 == 0 else ints[i + 2]
            ints[ints[i + 3]] = p_1 + p_2
            i += 4
        elif opcode == 2:
            # pos3 = pos1 * pos2
            p_1 = ints[ints[i + 1]] if mode_1 == 0 else ints[i + 1]
            p_2 = ints[ints[i + 2]] if mode_2 == 0 else ints[i + 2]
            ints[ints[i + 3]] = p_1 * p_2
            i += 4
        elif opcode == 3:
            # pos3 = input
            ints[ints[i + 1]] = input_value
            i += 2
        elif opcode == 4:
            # pos4 = output
            print(ints[ints[i + 1]])
            i += 2
        elif opcode == 5:
            p_1 = ints[ints[i + 1]] if mode_1 == 0 else ints[i + 1]
            p_2 = ints[ints[i + 2]] if mode_2 == 0 else ints[i + 2]
            if p_1 != 0:
                i = p_2
            else:
                i += 3
        elif opcode == 6:
            p_1 = ints[ints[i + 1]] if mode_1 == 0 else ints[i + 1]
            p_2 = ints[ints[i + 2]] if mode_2 == 0 else ints[i + 2]
            if p_1 == 0:
                i = p_2
            else:
                i += 3
        elif opcode == 7:
            p_1 = ints[ints[i + 1]] if mode_1 == 0 else ints[i + 1]
            p_2 = ints[ints[i + 2]] if mode_2 == 0 else ints[i + 2]
            ints[ints[i + 3]] = 1 if p_1 < p_2 else 0
            i += 4
        elif opcode == 8:
            p_1 = ints[ints[i + 1]] if mode_1 == 0 else ints[i + 1]
            p_2 = ints[ints[i + 2]] if mode_2 == 0 else ints[i + 2]
            ints[ints[i + 3]] = 1 if p_1 == p_2 else 0
            i += 4
        else:
            raise Exception("invalid opcode at index-ish: ", ints[i:i+5])


def main():
    """ Entrypoint for calling the script from CLI. """

    # solve("05-test-eq-8.in", 8)
    # solve("05-test-le-8.in", 8)

    solve("05.in", 1)
    solve("05.in", 5)

    return 0


if __name__ == "__main__":
    sys.exit(main())
