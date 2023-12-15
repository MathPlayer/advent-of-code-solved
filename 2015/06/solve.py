#!/usr/bin/env python3

filename = 'input'
with open(filename) as f:
    data = [x.strip().split() for x in f.readlines()]

lights = [[0] * 1000 for _ in range(1000)]
for order in data:
    if order[0] == "toggle":
        start = [int(x) for x in order[1].split(",")]
        stop = [int(x) for x in order[-1].split(",")]
        for i in range(start[0], stop[0] + 1):
            for j in range(start[1], stop[1] + 1):
                lights[i][j] = 1 - lights[i][j]
    elif order[0] == "turn":
        value = 1 if order[1] == "on" else 0
        start = [int(x) for x in order[2].split(",")]
        stop = [int(x) for x in order[-1].split(",")]
        for i in range(start[0], stop[0] + 1):
            for j in range(start[1], stop[1] + 1):
                lights[i][j] = value
print(sum(map(sum, lights)))

lights = [[0] * 1000 for _ in range(1000)]
for order in data:
    if order[0] == "toggle":
        start = [int(x) for x in order[1].split(",")]
        stop = [int(x) for x in order[-1].split(",")]
        for i in range(start[0], stop[0] + 1):
            for j in range(start[1], stop[1] + 1):
                lights[i][j] += 2
    elif order[0] == "turn":
        value = 1 if order[1] == "on" else -1
        start = [int(x) for x in order[2].split(",")]
        stop = [int(x) for x in order[-1].split(",")]
        for i in range(start[0], stop[0] + 1):
            for j in range(start[1], stop[1] + 1):
                lights[i][j] = max(0, lights[i][j] + value)
print(sum(map(sum, lights)))
