#!/usr/bin/env python

import sys
import re

from collections import Counter

def read(in_file):
    # Form groups of (<X>-<Y> <CHAR>: <PW>).
    r = re.compile('([0-9]+)-([0-9]+) ([a-z]): (.*)')
    with open(in_file) as f:
        data = [m.groups() for m in map(lambda x: r.match(x), (x.strip() for x in f.readlines()))]
    return data


def is_valid_part_1(one_pw_data):
    count_min, count_max, char, pw = one_pw_data
    count_min, count_max = int(count_min), int(count_max)
    count = Counter(pw)[char]
    return count_min <= count and count <= count_max


def is_valid_part_2(one_pw_data):
    fst, snd, char, pw = one_pw_data
    fst, snd = int(fst) - 1, int(snd) - 1
    return (pw[fst] == char and pw[snd] != char) or (pw[fst] != char and pw[snd] == char)


def solve(in_file):
    ''' Solves day 02. '''
    pw_data = read(in_file)
    print(sum(map(is_valid_part_1, pw_data)))
    print(sum(map(is_valid_part_2, pw_data)))


if __name__ == '__main__':
    solve('02test.in')
    solve('02.in')

    sys.exit(0)