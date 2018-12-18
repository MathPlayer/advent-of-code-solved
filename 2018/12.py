#!/usr/bin/env python3


def read_data(filename):
    state = None
    pots = set()
    with open(filename) as f:
        for line in map(str.strip, f):
            if not line:
                continue
            if line.startswith("initial state: "):
                state = line.split(": ")[1]
            else:
                k, v = line.split(" => ")
                if v == "#":
                    pots.add(k)
    return (state, pots)


def score(state, index):
    s = 0
    for i in range(len(state)):
        if state[i] == "#":
            s += i + index
    return s


def solve(state, pots, generations):
    index = 0
    scores = {}
    passes = 20
    for g in range(generations):
        if g % 1000 == 0:
            print(g, index, state)
        # extend state if needed
        if not state.startswith("....."):
            state = "....." + state
            index -= 5
        if not state.endswith("....."):
            state = state + "....."

        # update state
        new_state = list(state)
        for x in range(len(state) - 5):
            new_state[x + 2] = "#" if "".join(state[x:x + 5]) in pots else "."
        state = "".join(new_state)
        key_index = state.index("#") - index
        key_state = state[state.index("#"):state.rindex("#") + 1]
        if key_state in scores:
            print("Repeat! ", g, score(state, index))
            passes -= 1
            if not passes:
                break
        scores[key_state] = score(state, index)

    return scores


state, pots = read_data("12test.in")
state, pots = read_data("12.in")
solve(state, pots, 20)
solve(state, pots, 50000000000)

# After a while, the pattern stays the same and translates to the left:
# Answer is 5510 + (50000000000 - 121) * 42 = 122100000000428
