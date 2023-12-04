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
    return points


def solve(data):
    results = {}
    for i, card in enumerate(data):
        results[i+1] = points(card[0], card[1])

    cards = {
        i+1: 1
        for i in range(len(results))
    }

    for i, count in cards.items():
        for j in range(results[i]):
            cards[i+j+1] += count

    print(sum(cards.values()))


filename = 'input'
# filename = 'test1'

data = read_lines(filename)
solve(data)
