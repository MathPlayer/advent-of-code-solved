#!/usr/bin/python

import sys
import re

r1 = re.compile(r"ab|cd|pq|xy")
r2 = re.compile(r"(.)\1")
r3 = re.compile(r"(.).\1")
r4 = re.compile(r"(..).*\1")

def is_nice1(string):
    if r1.search(string):
        return False

    if sum(map(string.lower().count, "aeiou")) < 3:
        return False

    if not r2.search(string):
        return False

    return True


def is_nice2(string):
    if not r3.search(string) or not r4.search(string):
        return False

    return True

if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = map(str.strip, f.readlines())

    print sum(map(is_nice1, data))
    print sum(map(is_nice2, data))
