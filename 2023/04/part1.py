#!/usr/bin/env python3


def read_lines(filename):
    with open(filename) as f:
        data = [
            line.strip().split(':')[1]
            for line in f.readlines()
        ]
    data = [
        line.split('|')
        for line in data
    ]
    data = [
        [[int(x) for x in half.strip().split()] for half in line]
        for line in data
    ]
    return data


def points(winning_numbers, numbers):
    points = 0
    for number in numbers:
        if number in winning_numbers:
            points += 1
    return 2 ** points >> 1


def solve(data):
    result = 0
    for i, card in enumerate(data):
        result += points(card[0], card[1])
    print(result)


filename = 'input'
# filename = 'test1'

data = read_lines(filename)
solve(data)
