#!/usr/bin/python

from collections import Counter
import string
import sys

def check_line(line):
    (split, checksum) = line.strip().strip("]").split("[")
    split = split.rsplit("-", 1)
    count = map(lambda x: x[0],
                sorted(Counter(split[0].replace("-", "")).most_common(),
                       key=lambda x: (-x[1], x[0]))[:len(checksum)])
    az = string.ascii_lowercase
    if "".join(count) != checksum:
        return 0

    sector = int(split[1])
    shift = sector % len(az)
    shifted = az[shift:] + az[:shift]
    trans = string.maketrans(az, shifted)
    if "pole" in split[0].translate(trans):
        print sector
    return sector

print sum(map(check_line, open(sys.argv[1]).readlines()))
