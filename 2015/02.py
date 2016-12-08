#!/usr/bin/python

from operator import mul
import sys

def paper_needed(sizes):
    s1 = 2 * sizes[0] * sizes[1]
    s2 = 2 * sizes[1] * sizes[2]
    s3 = 2 * sizes[0] * sizes[2]

    return s1 + s2 + s3 + min(s1, s2, s3) / 2

def ribbon_needed(sizes):
    volume = reduce(mul, sizes)
    return volume + (sum(sizes) - max(sizes)) * 2

if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = map(lambda x: map(int, x.strip().split("x")), f.readlines())

    if not data:
        sys.exit(-1)

    print sum(map(paper_needed, data))
    print sum(map(ribbon_needed, data))
