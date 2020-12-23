#!/usr/bin/env python

import sys

def shuffle(cups, steps):
    ''' Simulates the crab shuffling for the given cups and steps countt. '''
    count = len(cups)
    min_cup = min(cups)
    max_cup = max(cups)

    # Build a linked list as dict of (node, next) pairs.
    d_cups = {cups[i]: cups[i + 1] for i in range(count - 1)}
    d_cups[cups[-1]] = cups[0]

    cup = cups[0]
    for _ in range(steps):
        # Pick cups.
        picked = []
        p = d_cups[cup]
        for _ in range(3):
            picked.append(p)
            p = d_cups[p]

        # Find the destination.
        dest = cup - 1
        if dest < min_cup:
            dest = max_cup
        while dest in picked:
            dest -= 1
            if dest < min_cup:
                dest = max_cup

        # Update the links.
        d_cups[cup] = d_cups[picked[-1]]   # Drop the picked after the cup.
        d_cups[picked[-1]] = d_cups[dest]  # Put next of dest after picked.
        d_cups[dest] = picked[0]           # Put picked after dest.

        # Move the crab.
        cup = d_cups[cup]

    return d_cups


def print_1(d_cups):
    ''' Prints the labels of the cups starting clockwise from cup 1 and excluding it. '''
    i = d_cups[1]
    result = []
    while len(result) < len(d_cups) - 1:
        result.append(i)
        i = d_cups[i]
    print(''.join(map(str, result)))


def print_2(d_cups):
    ''' Prints the first 2 cups after cup 1 and their product. '''
    fst = d_cups[1]
    snd = d_cups[fst]
    print(fst, snd, fst * snd)


def input_1(string):
    ''' Creates a list of ints from the string. '''
    return [int(c) for c in string]


def input_2(string):
    ''' Creates a list of ints from the string + adding the numbers from max+1 to 1 million. '''
    cups = input_1(string)
    return cups + [x for x in range(max(cups) + 1, 10**6 + 1)]


if __name__ == '__main__':
    example = '389125467'
    my_input = '362981754'

    print("Part 1")
    print_1(shuffle(input_1(example), 10))
    print_1(shuffle(input_1(example), 100))
    print_1(shuffle(input_1(my_input), 100))

    print("Part 2")
    print_2(shuffle(input_2(example), 10**7))
    print_2(shuffle(input_2(my_input), 10**7))

    sys.exit(0)
