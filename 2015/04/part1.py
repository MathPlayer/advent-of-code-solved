#!/usr/bin/env python3

filename = 'input'

data = open(filename).read().strip()
print(data)


def md5(s):
    import hashlib
    return hashlib.md5(s.encode()).hexdigest()


i = 0
while True:
    if md5(data + str(i))[:5] == '00000':
        print(i)
        break
    i += 1
