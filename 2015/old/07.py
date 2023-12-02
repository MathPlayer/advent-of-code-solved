#!/usr/bin/python

import sys


def convert(d, key):
    if key in d:
        return d[key]
    if key.isdigit():
        return int(key)
    return None


def compute(data):
    d = {}
    while True:
        new_data = []
        lenght = len(data)
        for l, r in data:
            l = l.split()
            if len(l) == 3:
                a = convert(d, l[0])
                b = convert(d, l[2])
                if a is None or b is None:
                    new_data.append([" ".join(l), r])
                elif l[1] == "AND":
                    d[r] = a & b
                elif l[1] == "OR":
                    d[r] = a | b
                elif l[1] == "RSHIFT":
                    d[r] = a >> b
                elif l[1] == "LSHIFT":
                    d[r] = a << b
                else:
                    raise Exception("Invalid operation: {}".format(l))
            elif len(l) == 2:
                a = convert(d, l[1])
                if a is None:
                    new_data.append([" ".join(l), r])
                elif l[0] == "NOT":
                    d[r] = ~a
                else:
                    raise Exception("Invalid operation: {}".format(l))
            elif len(l) == 1:
                a = convert(d, l[0])
                if a is None:
                    new_data.append([" ".join(l), r])
                else:
                    d[r] = a

        if not new_data or lenght == len(new_data):
            break
        data = new_data[:]

    return d


if __name__ == "__main__":
    data = None
    with open(sys.argv[1], "r") as f:
        data = map(lambda x: x.strip().split(" -> "), f.readlines())

    d = compute(data)
    print d["a"]

    new_data = []
    for l, r in data:
        if r != "b":
            new_data.append([l, r])
        else:
            new_data.append([str(d["a"]), r])

    d = compute(new_data)
    print d["a"]

    sys.exit(0)
