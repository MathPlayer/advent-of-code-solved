#!/usr/bin/env python3

from collections import Counter

data = open("input").read()
level = 0
for i, c in enumerate(data):
    if c == '(':
        level += 1
    elif c == ')':
        level -= 1
    if level == -1:
        print(i + 1)
        break

