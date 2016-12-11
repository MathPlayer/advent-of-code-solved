#!/usr/bin/python


def solve(matrix, sequence):
    for op in map(str.split, sequence):
        if op[0] == "rect":
            (a, b) = map(int, op[1].split("x"))
            for i in xrange(a):
                for j in xrange(b):
                    matrix[j][i] = 1
        elif op[0] == "rotate":
            index = int(op[2][2:])
            shift = int(op[-1])
            if op[1] == "column":
                matrix = map(list, zip(*matrix))
                shift = (len(matrix[0]) - shift) % len(matrix[0])
                matrix[index] = matrix[index][shift:] + matrix[index][:shift]
                matrix = map(list, zip(*matrix))
            elif op[1] == "row":
                shift = (len(matrix[0]) - shift) % len(matrix[0])
                matrix[index] = matrix[index][shift:] + matrix[index][:shift]

    return matrix


print solve([[0 for _ in xrange(7)] for _ in xrange(3)],
            ["rect 3x2",
             "rotate column x=1 by 1",
             "rotate row y=0 by 4",
             "rotate column x=1 by 1"])

matrix = solve([[0 for _ in xrange(50)] for _ in xrange(6)],
               open("08.in").readlines())
print sum(map(sum, matrix))
for a in xrange(len(matrix)):
    print "".join(map(lambda x: "@" if x else " ", matrix[a]))

