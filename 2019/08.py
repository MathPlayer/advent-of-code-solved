#!/usr/bin/env python3
""" Solving 08 advent 2019. """

from collections import Counter


def read(filename):
    """ read input data. """
    with open(filename) as input_file:
        lines = list(map(str.strip, input_file.readlines()))

    digits = []
    for line in lines:
        for c in line:
            digits.append(int(c))

    return digits


def solve_1(filename, width, height):
    """ Solve day 08 part 1. """
    digits = read(filename)

    layers = [digits[i:i + width * height] for i in range(0, len(digits), width * height)]
    counters = [Counter(layer) for layer in layers]
    min_zeros = min(counters, key=lambda x: x[0])
    print(min_zeros)
    print(min_zeros[1] * min_zeros[2])


def print_layer(a_layer, width):
    for index in range(0, len(a_layer), width):
        print("".join(map(str, a_layer[index:index + width])).replace('0', ' ').replace('1', '#'))


def solve_2(filename, width, height):
    """ Solve day 08 part 2. """
    digits = read(filename)

    layers = [digits[i:i + width * height] for i in range(0, len(digits), width * height)]
    final = [2] * width * height
    for layer in layers:
        for (i, v) in enumerate(layer):
            if final[i] != 2:
                continue
            final[i] = v

    print_layer(final, width)


if __name__ == "__main__":
    solve_1("08-example.in", 3, 2)
    solve_1("08.in", 25, 6)

    solve_2("08-example-2.in", 2, 2)
    solve_2("08.in", 25, 6)
