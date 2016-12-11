#!/usr/bin/python

import sys
from hashlib import md5


def get_pass1(s):
    i = 0
    ret = ""
    while len(ret) < 8:
        h = md5(s + str(i)).hexdigest()
        if h.startswith("00000"):
            ret += h[5]
            print "{0:10d} {1}".format(i, ret)
        i += 1
        if not i % 100000:
            print i
    return ret

def get_pass2(s):
    i = 0
    ret = ["*"] * 8
    while "*" in ret:
        h = md5(s + str(i)).hexdigest()
        if (h.startswith("00000") and h[5] in "01234567" and
            ret[int(h[5])] == "*"):
            ret[int(h[5])] = h[6]
            print "{0:10d} {1}".format(i, "".join(ret))
        i += 1
        if not i % 100000:
            print i
    return "".join(ret)

if sys.argv[1] == "1":
    if get_pass("abc") == "18f47a30":
        print get_pass("reyedfim")
elif sys.argv[1] == "2":
    if get_pass2("abc") == "05ace8e3":
        print get_pass2("reyedfim")
