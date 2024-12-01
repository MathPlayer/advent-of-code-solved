#!/usr/bin/env python3


def read(filename):
    data = open(filename).readlines()
    data = [x.strip() for x in data]

    data = [list(map(int, x.split())) for x in data]
    data = [list(x) for x in zip(*data)]

    return data


def part_1(data):
    fst = sorted(data[0])
    snd = sorted(data[1])

    result = 0
    for (i, j) in zip(fst, snd):
        result += abs(i - j)

    print(result)


def part_2(data):
    fst = sorted(data[0])
    snd = sorted(data[1])

    result = 0
    for i in fst:
        result += i * snd.count(i)

    print(result)


def solve(filename):
    data = read(filename)

    print("part 1:")
    part_1(data)

    print("part 2:")
    part_2(data)


if __name__ == '__main__':
    solve('input')