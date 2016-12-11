#!/usr/bin/python

import re
import sys


r = re.compile(r"\\x[0-9A-Fa-f][0-9A-Fa-f]")


def get_memory_size(string):
    return len(r.sub("X",
                     string[1:-1].replace("\\\\", "\\").replace("\\\"", "\"")))


def encode_size(string):
    return len(string.replace("\\", "\\\\").replace("\"", "\\\"")) + 2


if __name__ == "__main__":
    data = map(str.strip, open(sys.argv[1]).readlines())
    print sum(map(lambda x: len(x) - get_memory_size(x), data))
    print sum(map(lambda x: encode_size(x) - len(x), data))
