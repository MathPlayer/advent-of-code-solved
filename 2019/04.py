#!/usr/bin/env python3
""" Solves day 4 of 2019. """

import sys


def valid_password(number):
    """ Checks for part 1 if a number can be a password. """
    digit = 10
    double = False
    while number > 0:
        last = number % 10
        if last > digit:
            return False
        if last == digit:
            double = True
        digit = last
        number //= 10

    return double

def valid_password_2(number):
    """ Checks for part 2 if a number can be a password. """
    digit = 10
    double = False
    exact_two = False
    double_count = 1
    while number > 0:
        last = number % 10
        number //= 10
        if last > digit:
            return False
        if last == digit:
            double = True
            double_count += 1
        if last < digit:
            if double_count == 2:
                exact_two = True
            double_count = 1
        digit = last

    return double and (exact_two or double_count == 2)


def main():
    """ Entrypoint for calling the script from CLI. """

    interval = [124075, 580769]

    print(valid_password(111111))
    print(valid_password(223450))
    print(valid_password(123789))

    counter = 0
    for i in range(interval[0], interval[1]):
        if valid_password(i):
            counter += 1
    print(counter)

    print(valid_password_2(111122))
    print(valid_password_2(123444))

    counter = 0
    for i in range(interval[0], interval[1]):
        if valid_password_2(i):
            counter += 1
    print(counter)


    return 0


if __name__ == "__main__":
    sys.exit(main())
