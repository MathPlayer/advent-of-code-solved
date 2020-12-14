#!/usr/bin/env python

import re
import sys

from copy import deepcopy

INSTR = re.compile(r"mem\[([^]]+)\] = ([0-9]+)")


def int_str_to_rev_bin_list(s, length=0):
    ''' Converts a string with an integer into a string with its binary format reversed (easier to iterate). '''
    return [c for c in f'{{0:0{length}b}}'.format(int(s))][::-1]


def rev_bin_list_to_int(rev_list):
    ''' Converts a list with a binary reversed number into int. '''
    return int(''.join(rev_list[::-1]), 2)


def mask_value(mask, value):
    ''' Apply mask to a value. '''
    value_len = len(value)
    for i, mask_val in enumerate(mask):
        if i >= value_len:
            value.append('0')
        if mask_val == '0':
            value[i] = '0'
        if mask_val == '1':
            value[i] = '1'
    return value


def mask_addr(mask, value):
    ''' Apply mask to a value. '''
    value_len = len(value)
    for i, mask_val in enumerate(mask):
        if i >= value_len:
            value.append('0')
        if mask_val == '1':
            value[i] = '1'
        if mask_val == 'X':
            value[i] = 'X'
    return value


def fill_addr(addr, values):
    ''' Fill X-es into addr from values. '''
    fill_count = 0
    new_addr = addr.copy()
    for i, value in enumerate(addr):
        if value == 'X':
            new_addr[i] = values[fill_count]
            fill_count += 1
    return new_addr


def read(in_file):
    ''' Reads data for day 14. '''
    data = []
    with open(in_file) as f:
        for line in map(lambda x: x.strip(), f.readlines()):
            if line.startswith('mask = '):
                data.append(('mask', line.lstrip('mask = ')[::-1]))
            else:
                groups = INSTR.match(line).groups()
                data.append((int_str_to_rev_bin_list(groups[0]), int_str_to_rev_bin_list(groups[1])))
    return data


def solve_1(data):
    ''' Solves part 1. '''
    mem = {}
    mask = None
    for (x, y) in data:
        if x == 'mask':
            mask = y
        else:
            mem[rev_bin_list_to_int(x)] = rev_bin_list_to_int(mask_value(mask, y))
    print(sum(mem.values()))


def solve_2(data):
    ''' Solves part 2. '''
    mem = {}
    mask = None
    for (x, y) in data:
        if x == 'mask':
            mask = y
        else:
            addr = mask_addr(mask, x)
            value = rev_bin_list_to_int(y)
            count = addr.count('X')
            if not count:
                mem[rev_bin_list_to_int(addr)] = value
            else:
                for combo in map(lambda x: int_str_to_rev_bin_list(x, count), range(2**count)):
                    mem[rev_bin_list_to_int(fill_addr(addr, combo))] = value
    print(sum(mem.values()))


def solve(in_file):
    ''' Solves day 14. '''
    data = read(in_file)
    print(in_file)
    solve_1(deepcopy(data))
    solve_2(deepcopy(data))


if __name__ == '__main__':
    # Don't run on part 2.
    # solve('14test.in')
    solve('14test2.in')
    solve('14.in')

    sys.exit(0)
