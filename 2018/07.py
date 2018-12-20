#!/usr/bin/env python3

import pdb


with open("07.in") as f_in:
# with open("07test.in") as f_in:
    deps = [[x[5], x[36]] for x in f_in.readlines()]

syms = sorted(set(item for sublist in deps for item in sublist))
syms_copy = sorted(set(syms))
deps_copy = list(deps)

r1 = []
while syms:
    for x in syms:
        if any(map(lambda dep: dep[1] == x, deps)):
            continue
        deps = filter(lambda dep: dep[0] != x, deps)
        r1 += x
        syms.remove(x)
        break

print("".join(r1))

syms = set(syms_copy)
deps = deps_copy

# work = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
work = {}

second = -1
while work or second == -1:
    # do work
    second += 1
    work = {k: v - 1 for (k, v) in work.items()}

    print("Second {} ---- work: {}".format(second, work))

    work_done = []
    for k, v in work.items():
        if v > 0:
            continue
        work_done.append(k)
        if k in syms:
            syms.remove(k)
        deps = filter(lambda dep: dep[0] != k, deps)

    for w in work_done:
        work.pop(w)

    if len(work) >= 5:
        print("- busy enough")
        continue

    # get available work
    print("-> check available work in syms {} deps {}".format(syms, deps))
    avail = []
    for x in syms:
        if any(map(lambda dep: dep[1] == x, deps)):
            continue
        if x in work:
            continue
        print("--> avail: {}".format(x))
        avail.append(x)

    if not avail:
        continue

    for x in avail:
        if len(work) >= 5:
            break
        print("starting work for {}".format(x))
        work[x] = 60 + ord(x) - ord('A') + 1
        # work[x] = ord(x) - ord('A') + 1

