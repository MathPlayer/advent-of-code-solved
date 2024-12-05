#!/usr/bin/env python3


def read(filename):
    data = open(filename).readlines()

    orders = []
    updates = []
    for line in data:
        if '|' in line:
            order = list(map(int, line.strip().split('|')))
            orders.append(order)
        elif ',' in line:
            update = list(map(int, line.strip().split(',')))
            updates.append(update)

    return orders, updates


def is_ordered(checked_update, orders):
    for x, y in orders:
        if x not in checked_update or y not in checked_update:
            continue
        index_x = checked_update.index(x)
        index_y = checked_update.index(y)
        if index_x >= index_y:
            return False

    return True


def part_1(data):
    result = 0
    orders, updates = data

    for update in updates:
        if is_ordered(update, orders):
            result += update[len(update) // 2]

    return result


def part_2(data):
    result = 0
    orders, updates = data

    for update in updates:
        if is_ordered(update, orders):
            continue

        ordered_update = []
        for number in update:
            if not ordered_update:
                ordered_update.append(number)
                continue

            # Try to add the number from right to left, while keeping the order.
            added = False
            i = len(ordered_update)
            while not added and i >= 0:
                if is_ordered(ordered_update[:i] + [number] + ordered_update[i:], orders):
                    ordered_update = ordered_update[:i] + [number] + ordered_update[i:]
                    added = True
                else:
                    i -= 1
            if not added:
                raise Exception(f"failed to add {number=} to {ordered_update=}.")

        # print(f"update: {update}, ordered_update: {ordered_update}")
        result += ordered_update[len(ordered_update) // 2]

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
