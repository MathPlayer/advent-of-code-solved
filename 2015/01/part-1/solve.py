#!/usr/bin/env python3

from collections import Counter

data = open("input").read()
c = Counter(data)
print(c['('] - c[')'])
