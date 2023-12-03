#!/usr/bin/env python3

import re

filename = 'input'
# filename = 'test'
data = [x.strip() for x in open(filename, 'r').readlines()]


def is_nice(s):
    pair = re.compile('(..).*\\1')
    repeat = re.compile('(.).\\1')

    if pair.search(s) and repeat.search(s):
        return True

    return False


count = 0
for s in data:
    if is_nice(s):
        count += 1
print(count)
