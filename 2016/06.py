#!/usr/bin/python

from collections import Counter

data = map(str.strip, open("06.in").readlines())
print "".join(map(lambda x: Counter(x).most_common(1)[0][0], zip(*data)))
print "".join(map(lambda x: Counter(x).most_common()[-1][0], zip(*data)))
