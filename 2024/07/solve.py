#!/usr/bin/env python3

OPERATORS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}


def read(filename):
    data = open(filename).readlines()
    data = [x.strip().split(':') for x in data]
    data = [(int(x[0]), [int(y) for y in x[1].strip().split()]) for x in data]

    return data


def fill_operators_1(total, equation, depth = 0):

    if len(equation) == 1:
        return equation[0] == total

    if fill_operators_1(total, [equation[0] + equation[1]] + equation[2:], depth + 1):
        return True

    if fill_operators_1(total, [equation[0] * equation[1]] + equation[2:], depth + 1):
        return True

    return False


def fill_operators_2(total, equation, depth = 0):

    if len(equation) == 1:
        return equation[0] == total

    if fill_operators_2(total, [equation[0] + equation[1]] + equation[2:], depth + 1):
        return True

    if fill_operators_2(total, [equation[0] * equation[1]] + equation[2:], depth + 1):
        return True

    if fill_operators_2(total, [int(str(equation[0]) + str(equation[1]))] + equation[2:], depth + 1):
        return True

    return False


def part_1(data):
    result = 0

    for total, equation in data:
        can_be_obtained = fill_operators_1(total, equation)
        if can_be_obtained:
            result += total

    return result


def part_2(data):
    result = 0

    for total, equation in data:
        can_be_obtained = fill_operators_2(total, equation)
        if can_be_obtained:
            result += total

    return result


def solve(filename):
    data = read(filename)

    print("part 1:")
    result = part_1(data)
    print(result)

    print("part 2:")
    result = part_2(data)
    print(result)


if __name__ == '__main__':
    # solve('test')
    solve('input')