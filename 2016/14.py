#!/usr/bin/python

import re
from hashlib import md5

key = re.compile(r'(\w)\1\1')

def keygen(salt, count, apply_count):
    i = 0
    d = {}
    keys = set()
    while len(keys) <= count:
        h = salt + str(i)
        for _ in xrange(apply_count):
            h = md5(h).hexdigest()
        to_delete = set()
        for (k, v) in d.iteritems():
            if i > k + 1000:
                to_delete.add(k)
                continue
            if k in to_delete:
                continue
            if v in h:
                print len(keys), k, i
                keys.add(k)
                to_delete.add(k)
                continue
        for delete in to_delete:
            del d[delete]
        m = key.search(h)
        if m:
            d[i] = "".join(m.groups(0)[0] * 5)
        i += 1
    return sorted(keys)

responses = []
for count in [1, 2017]:
    for salt in ["abc", "jlmsuwbz"]:
        ret = keygen(salt, 64, count)
        print ret[63:]
