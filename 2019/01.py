#!/usr/bin/env python3
""" Solves day 01 of 2019. """

import sys


def read(filename):
    """ Reads input data. """
    with open(filename) as input_file:
        file_data = [int(x) for x in input_file.read().strip().split()]

    return file_data


def fuel_1(mass):
    """ Computes the fuel needed for a given mass. """
    return mass // 3 - 2


def fuel_2(mass):
    """ Computes the fuel needed for a given mass and its associated fuel. """
    ret = 0
    fuel = fuel_1(mass)
    while fuel > 0:
        ret += fuel
        fuel = fuel_1(fuel)
    return ret


def solve(modules, fuel_mode):
    """ Solves day 1. """
    return sum(map(fuel_mode, modules))


def main():
    """ Entrypoint for calling the script from CLI. """

    # Examples.
    print(fuel_1(12))
    print(fuel_1(14))
    print(fuel_1(1969))
    print(fuel_1(100756))
    print(fuel_2(12))
    print(fuel_2(1969))
    print(fuel_2(100756))

    # Personal input.
    modules = read("01.in")

    # Solution.
    print(solve(modules, fuel_1))
    print(solve(modules, fuel_2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
