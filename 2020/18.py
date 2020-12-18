#!/usr/bin/env python

import sys

def read(in_file):
    ''' Reads data for day 18. '''
    with open(in_file) as f:
        # Add spaces around parantheses where needed.
        return tuple(map(lambda x: x.strip().replace('(', '( ').replace(')', ' )').split(), f.readlines()))


def reduce(stack):
    ''' Reduces one operation in the last enclsure on the stack. '''
    y = stack[-1].pop()
    op = stack[-1].pop()
    x = stack[-1].pop()
    if op == '+':
        stack[-1].append(x + y)
    elif op == '*':
        stack[-1].append(x * y)


def evaluate_1(expression):
    ''' Evaluates an expression of ints, '+', '*', '(' and ')' with no operator precedence (part 1). '''
    stack = [[]]
    for elem in expression:
        if elem in ['+', '*']:
            stack[-1].append(elem)
        elif elem == '(':
            stack.append([])
        elif elem == ')':
            # There should be only one value in the popped enclosure.
            val = stack.pop()
            stack[-1].append(val[0])
        else:
            stack[-1].append(int(elem))
        # Reduce the last enclsure.
        if len(stack[-1]) >= 3:
            reduce(stack)
    return stack[-1][0]


def evaluate_2(expression):
    ''' Evaluates an expression of ints, '+', '*', '(' and ')' with '+' precedence over '*' (part 2). '''
    stack = [[]]
    for elem in expression:
        if elem in ['+', '*']:
            stack[-1].append(elem)
        elif elem == '(':
            stack.append([])
        elif elem == ')':
            # Reduce all '*' in the last enclsure.
            while len(stack[-1]) >= 3:
                reduce(stack)
            # There should be only one value left in the popped enclosure.
            val = stack.pop()
            stack[-1].append(val[0])
        else:
            stack[-1].append(int(elem))
        # Reduce '+' in the last enclsure.
        if len(stack[-1]) >= 3 and stack[-1][-2] == '+':
            reduce(stack)
    # Reduce all '*'.
    while len(stack[-1]) >= 3:
        reduce(stack)
    return stack.pop()[0]


def solve(in_file):
    ''' Solves day 18. '''
    data = read(in_file)
    print(f"--- {in_file}")
    print(sum(map(evaluate_1, data)))
    print(sum(map(evaluate_2, data)))


if __name__ == '__main__':
    solve('18test.in')
    solve('18test2.in')
    solve('18.in')

    sys.exit(0)
