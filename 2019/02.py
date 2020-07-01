#!/usr/bin/env python3
""" Solves day 02 of 2019. """

import sys


def read(filename):
    """ Reads input data. """
    with open(filename) as input_file:
        file_data = [int(x) for x in input_file.read().strip().split(",")]

    return file_data


def solve(numbers, noun, verb):
    """ Solves day 2. """
    index = 0
    numbers[1] = noun
    numbers[2] = verb
    while True:
        if numbers[index] == 1:
            numbers[numbers[index+3]] = numbers[numbers[index+2]] + numbers[numbers[index+1]]
        elif numbers[index] == 2:
            numbers[numbers[index+3]] = numbers[numbers[index+2]] * numbers[numbers[index+1]]
        elif numbers[index] == 99:
            break
        index += 4

    return numbers[0]


def main():
    """ Entrypoint for calling the script from CLI. """

    ints = read("02.in")
    value = solve([x for x in ints], 12, 2)
    print(value)

    value = 19690720
    for i in range(100):
        for j in range(100):
            new_value = solve([x for x in ints], i, j)
            # print(i, j, new_value)
            if new_value == value:
                print(100 * i + j)
                return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
