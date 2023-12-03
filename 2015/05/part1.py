#!/usr/bin/env python3

filename = 'input'
data = open(filename, 'r').readlines()


def is_nice(s):
    if 'ab' in s:
        return False
    if 'cd' in s:
        return False
    if 'pq' in s:
        return False
    if 'xy' in s:
        return False

    vowels = 0
    for c in s:
        if c in 'aeiou':
            vowels += 1
            if vowels == 3:
                break
    if vowels < 3:
        return False

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


count = 0
for s in data:
    if is_nice(s):
        count += 1
print(count)
