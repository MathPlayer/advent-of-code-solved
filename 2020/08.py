#!/usr/bin/env python

import sys

from copy import deepcopy

def read(in_file):
    ''' Reads data as list of (instr, code) pairs for day 08. '''
    with open(in_file) as f:
        data = list(map(lambda pair: (pair[0], int(pair[1])), (x.strip().split() for x in f.readlines())))
    return data


def execute(data):
    ''' Executes the program using data. Returns (acc, flag) where flag is True on infinite loop detection or False when
    program ends. '''

    index = 0
    acc = 0

    visited = set()
    while True:
        if index in visited:
            return (acc, True)
        if index >= len(data):
            return (acc, False)
        op, code = data[index]
        visited.add(index)
        if op == 'acc':
            acc += code
            index += 1
        elif op == 'jmp':
            index += code
        elif op == 'nop':
            index += 1
    return acc


def solve(in_file):
    ''' Solves day 08. '''
    data = read(in_file)
    print(in_file)

    #part 1
    acc, _ = execute(data)
    print(acc)

    # part 2
    for i, (instr, code) in enumerate(data):
        if instr == 'jmp':
            copy = deepcopy(data)
            copy[i] = ('nop', code)
            acc, loop = execute(copy)
            if not loop:
                print(acc)
                return


if __name__ == '__main__':
    solve('08test.in')
    solve('08.in')

    sys.exit(0)
