#!/usr/bin/env python

def read_comma_separated(filename):
    with open(filename) as f:
        data = f.read().strip().split(',')

    return data


def get_hash(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256

    return current


def solve():
    # h = get_hash('HASH')
    # print(h)

    filename = 'test'
    filename = 'input'

    data = read_comma_separated(filename)
    s = 0
    for step in data:
        h = get_hash(step)
        # print(f"{step=} {h=}")
        s += h
    print(s)

    print("DONE")


solve()
