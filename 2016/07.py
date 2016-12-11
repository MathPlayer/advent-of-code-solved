#!/usr/bin/python

import re

r1 = re.compile(r"(\w)(?!\1)(\w)\2\1")
r2 = re.compile(r"\[[^\]]*(\w)(?!\1)(\w)\2\1[^\]]*\]")

def match1(s):
    return 1 if r1.search(s) and not r2.search(s) else 0


tests1 = ["abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui",
          "ioxxoj[asdfgh]zxcvbn"]
print map(match1, tests1)
print sum(map(match1, open("07.in").readlines()))

r3 = re.compile(r"\[[^\]]*\]")
r4 = re.compile(r"(?=(\w)(?!\1)(\w)\1)")
def match2(s):
    aux = reduce(lambda x, y: [x[0].replace(y, "|"), x[1] + [y[1:-1]]],
                r3.findall(s),
                [s, []])
    for match in map(r4.findall, aux[1]):
        for (a, b) in match:
            if b+a+b in aux[0]:
                return 1
    return 0


tests2 = ["aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb",
          "baba[abab]asdf", "qwq[ere]rer[wqw]ads"]
print map(match2, tests2)
print sum(map(match2, open("07.in").readlines()))
