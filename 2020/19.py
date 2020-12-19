#!/usr/bin/env python

import re
import sys

def read(in_file):
    ''' Reads data for day 19. '''

    def read_ints(from_str):
        return list(map(int, from_str.split()))

    rules = {}
    messages = []
    with open(in_file) as f:
        for line in map(lambda x: x.strip(), f.readlines()):
            if ':' in line:
                index, rule = line.split(':')
                if '|' in rule:
                    left, right = rule.split('|')
                    rules[int(index)] = read_ints(left.strip()) + ["|"] + read_ints(right.strip())
                elif any(x.isdigit() for x in rule):
                    rules[int(index)] = read_ints(rule)
                else:
                    rules[int(index)] = rule.replace('"', '').strip()

            elif line:
                messages.append(line)

    return rules, messages

def expand(rules, expanded, rule):
    ''' Recursively expands a rule based on the given rules and expanded cache. '''
    # Expand rule until only letters.
    result = []
    for elem in rule:
        if elem == '|':
            result.append("|")
        elif str(elem).isalpha():
            result.append(elem)
        elif elem in expanded:
            result.append(expanded[elem])
        elif elem in rules:
            new_expanded = expand(rules, expanded, rules[elem])
            expanded[elem] = new_expanded
            result.append(new_expanded)
        else:
            raise NotImplementedError(f'Why are we here? {elem}')
    result = '(' + ''.join(result) + ')' if len(result) > 1 else ''.join(result)
    return result


def solve_1(rules, messages):
    ''' Solves part 1. '''
    expanded = {}
    for index, rule in rules.items():
        expanded[index] = expand(rules, expanded, rule)

    r = re.compile('^' + expanded[0] + '$')
    print(sum(map(lambda x: True if r.match(x) else False, messages)))


def valid_2(msg, re_left, re_right):
    ''' Checks for msg to be valid for solving part 2. '''
    # There must be at least 2 left matches.
    for _ in range(2):
        sub_left = re_left.sub('', msg)
        if sub_left == msg:
            return False
        msg = sub_left

    # There must be at least 1 right match.
    sub_right = re_right.sub('', msg)
    if sub_right == msg:
        return False
    msg = sub_right

    # Every possible right match must have a corresponding left match...
    while msg:
        sub_right = re_right.sub('', msg)
        if sub_right == msg:
            break
        sub_left = re_left.sub('', sub_right)
        if sub_left == sub_right:
            return False
        msg = sub_left

    # ... and there might be more left matches.
    while msg:
        sub_left = re_left.sub('', msg)
        if sub_left == msg:
            return False
        msg = sub_left

    return len(msg) == 0


def solve_2(rules, messages):
    '''
    Original:
    8: 42
    11: 42 31
    Updated:
    8: 42 | 42 8
    11: 42 31 | 42 11 31
    The main rule (0):
    0: 8 11

    Checks for matching rule[42]{x times} on the left and rule[31]{y times} on the right, where x >= 2 and x >= y + 1.
    '''
    expanded = {}
    for index, rule in rules.items():
        if index not in [0, 8, 11]:
            expanded[index] = expand(rules, expanded, rule)

    re_left = re.compile('^' + expanded[42])
    re_right = re.compile(expanded[31] + '$')
    print(sum(map(lambda x: True if valid_2(x, re_left, re_right) else False, messages)))


def solve(in_file, solve_part_2=True):
    ''' Solves day 19. '''
    data = read(in_file)
    print(f"--- {in_file}")
    solve_1(data[0], data[1])
    if solve_part_2:
        solve_2(data[0], data[1])


if __name__ == '__main__':
    solve('19test.in', False)
    solve('19test2.in')
    solve('19.in')

    sys.exit(0)
