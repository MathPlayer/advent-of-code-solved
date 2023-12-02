#!/usr/bin/python

import sys
from hashlib import md5

if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = f.readline().strip()

    i = 0
    while True:
        if md5(data + str(i)).hexdigest().startswith("00000"):
            print i
            break
        i += 1

    while True:
        if md5(data + str(i)).hexdigest().startswith("000000"):
            print i
            break
        i += 1

    sys.exit(0)

