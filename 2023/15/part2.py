#!/usr/bin/env python

def read_comma_separated(filename):
    with open(filename) as f:
        data = f.read().strip().split(',')

    return data


def get_hash(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256

    return current


def print_boxes(boxes):
    for i in range(256):
        if boxes[i]:
            print(f"{i:3} {boxes[i]}")


def solve():
    # h = get_hash('HASH')
    # print(h)

    filename = 'test'
    filename = 'input'

    data = read_comma_separated(filename)

    boxes = {i: {} for i in range(256)}
    for step in data:
        if '-' in step:
            label, rest = step.split('-')[:2]
            h = get_hash(label)
            if label in boxes[h]:
                del boxes[h][label]

        elif '=' in step:
            label, rest = step.split('=')[:2]
            h = get_hash(label)
            boxes[h][label] = int(rest)
        else:
            print(f"INVALID {step=}")

    focus_power = 0
    for box_i, box in boxes.items():
        for lens_i, (label, power) in enumerate(box.items()):
            focus_power += (box_i + 1) * (lens_i + 1) * power
    print(focus_power)

    print("DONE")


solve()
