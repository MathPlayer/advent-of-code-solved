#!/usr/bin/env python3

from collections import defaultdict

GOOD = '.'
DAMAGED = '#'
UNKNOWN = '?'


def read_rows(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def parse_springs(line):
    springs, sizes = line.split()
    sizes = tuple(int(x) for x in sizes.split(','))
    return springs, sizes


def nfa_matches(springs, sizes):
    # Build and run an NFA on springs.
    # The NFA has one GOOD state between all springs.
    # For example, given sizes (1,2,3), the NFA would be '.#.##.###.'

    nfa = [GOOD]
    for spring_size in sizes:
        nfa.extend([DAMAGED] * spring_size)
        nfa.append(GOOD)
    # print(nfa)

    # State count (index in states: how many times it was visited)
    states = defaultdict()
    states[0] = 1
    # print(dict(states))

    # Run on the springs and adjust the states.
    # First GOOD matches the initial state.
    # Last GOOD moves all states in the final state, to have only one state to count.
    for spring in f"{GOOD}{springs}{GOOD}":
        # print("parsing spring", spring)
        new_states = defaultdict(int)
        for index, count in states.items():
            if nfa[index] == GOOD:
                if spring in [GOOD, UNKNOWN]:
                    new_states[index] += count
                if spring in [DAMAGED, UNKNOWN] and index != len(nfa) - 1:
                    new_states[index + 1] += count
            if nfa[index] == DAMAGED:
                if spring in [DAMAGED, UNKNOWN] and index != len(nfa) - 1 and nfa[index + 1] == DAMAGED:
                    new_states[index + 1] += count
                if spring in [GOOD, UNKNOWN] and index != len(nfa) - 1 and nfa[index + 1] == GOOD:
                    new_states[index + 1] += count

        states = new_states
        # print(dict(states))

    return states[len(nfa) - 1]


def solve(filename):
    data = read_rows(filename)

    result = 0
    for i, line in enumerate(data):
        springs, sizes = parse_springs(line)
        result += nfa_matches(springs, sizes)
    print(result)

    result = 0
    for i, line in enumerate(data):
        springs, sizes = parse_springs(line)
        springs = '?'.join([springs for _ in range(5)])
        sizes = sizes * 5
        result += nfa_matches(springs, sizes)
    print(result)


filename = 'test'
filename = 'test2'
filename = 'input'

solve(filename)
