#!/usr/bin/env python

filename = 'input'
# filename = 'test'
data = open(filename).read()

sum = 0
for entry in data.splitlines():
    first, last = None, None
    for c in entry:
        if c.isdigit():
            if not first:
                first = int(c)
            last = int(c)
    if first and last:
        print(f"{entry} adding {first} {last}")
        sum += first * 10 + last

print(sum)
