#!/usr/bin/env python3


def power(x, y, gsn):
    rack_id = x + 10
    return (((rack_id * y + gsn) * rack_id) // 100) % 10 - 5


print(4, power(3, 5, 8))
print(-5, power(122, 79, 57))
print(0, power(217, 196, 39))
print(4, power(101, 153, 71))


def compute_grid(size_x, size_y, gsn):
    return [[power(x, y, gsn) for y in range(size_y)] for x in range(size_x)]


def solve(gsn, size):
    g = compute_grid(300, 300, gsn)
    total = -90000000
    total_x = -1
    total_y = -1
    for x in range(len(g) - size + 1):
        for y in range(len(g[0]) - size + 1):
            s = 0
            for k in range(size):
                s += sum(g[x + k][y:y + size])
            if total < s:
                total_x = x
                total_y = y
                total = s
    print(total, total_x, total_y, size, sep=",")


solve(18, 3)
solve(3628, 3)
for i in range(2, 299):
    # visual matching on total score. for size big enough, the values will go below 0.
    solve(3628, i)
