#!/usr/bin/env python3

from collections import Counter

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
RANK_DICT = {r: i for i, r in enumerate(reversed(CARDS))}


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def parse_lines(data):
    result = []
    for line in data:
        cards, bid = line.split()
        bid = int(bid)
        result.append((cards, bid))
    return result


def get_hand_rank(hand):
    ranks = sorted([RANK_DICT[r] for r in hand], reverse=True)
    rank_counts = Counter(ranks)

    if len(rank_counts) == 5:
        return 0
    elif len(rank_counts) == 4:
        return 1
    elif len(rank_counts) == 3:
        mc = rank_counts.most_common(2)
        if mc[0][1] == 3:
            return 3
        else:
            return 2
    elif len(rank_counts) == 2:
        mc = rank_counts.most_common(1)[0]
        if mc[1] == 4:
            return 5
        else:
            return 4
    return 6


def add_hand_rank(data, func):
    result = []
    for hand, bid in data:
        rank = func(hand)
        result.append((rank, [RANK_DICT[r] for r in hand], hand, bid))
    return result


def solve(data):
    sorted_hands = sorted(data)
    result = 0
    for i, (rank, ranks, hand, bid) in enumerate(sorted_hands):
        result += (i+1) * bid
    print(result)


filename = 'input'
# filename = 'test'

data = read_lines(filename)
data = parse_lines(data)
data = add_hand_rank(data, get_hand_rank)
solve(data)
