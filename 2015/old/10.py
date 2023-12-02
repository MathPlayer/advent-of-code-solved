#!/usr/bin/python

def las(string):
    ret = ""
    prev = None
    count = 0
    for c in string:
        if not prev:
            prev = c
            count = 1
            continue
        if c == prev:
            count += 1
            continue
        else:
            ret += str(count) + prev
            prev = c
            count = 1
    if not prev:
        return "1"
    return ret + str(count) + prev

s = "1113122113"
for i in xrange(50):
    s = las(s)
    print i+1, len(s)
