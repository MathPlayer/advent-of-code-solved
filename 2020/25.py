#!/usr/bin/env python

import sys


def update(value, subject):
    ''' Runs one step of tthe algoryhm encryption on the value using the subject. '''
    return (value * subject) % 20201227


def find_loop_size(subject, key):
    ''' Runs the algorythm encryption on subject until it finds the key. Returns the loop size. '''
    loop = 0
    value = 1
    while value != key:
        loop += 1
        value = update(value, subject)
    return loop


def transform(subject, loop_size):
    ''' Runs the algorythm encrypttion on subject for loop_size times. Returns the result. '''
    value = 1
    for _ in range(loop_size):
        value = update(value, subject)
    return value


# Card and door have different loop sizes.
if __name__ == '__main__':
    # Part 1 example
    print(f"Example: {find_loop_size(7, 5764801)} should be 8")
    print(f"Example: {find_loop_size(7, 17807724)} should be 11")

    # Part 1
    card_key = 6270530
    door_key = 14540258

    card_loop_size = find_loop_size(7, card_key)
    print(f"Card loop size: {card_loop_size}")

    door_loop_size = find_loop_size(7, door_key)
    print(f"Door loop size: {door_loop_size}")

    card_computed_key = transform(door_key, card_loop_size)
    print(f"Card computed encryption: {card_computed_key}")

    door_computed_key = transform(card_key, door_loop_size)
    print(f"Door computed encryption: {door_computed_key}")

    # Part 2 is for free if you solved everything else.

    sys.exit(0)
