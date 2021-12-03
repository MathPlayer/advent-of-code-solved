# filename = 'input-test.txt'
filename = 'input.txt'
init_data = [x.strip() for x in open(filename, 'r').readlines()]
size = len(init_data[0])


def get_counts(data, pos):
    counts = [0, 0]
    for s in data:
        counts[int(s[pos])] += 1
    return counts


def keep_o2(counts, elem, i):
    if counts[0] > counts[1] and elem[i] == '0':
        return True
    if counts[0] < counts[1] and elem[i] == '1':
        return True
    if counts[0] == counts[1] and elem[i] == '1':
        return True
    return False


def keep_co2(counts, elem, i):
    if counts[0] < counts[1] and elem[i] == '0':
        return True
    if counts[0] > counts[1] and elem[i] == '1':
        return True
    if counts[0] == counts[1] and elem[i] == '0':
        return True
    return False


def find_number(data, func):
    for i in range(size):
        counts = get_counts(data, i)
        data = [x for x in data if func(counts, x, i)]
        if len(data) == 1:
            return data[0]
    raise Exception(f"Why are there more numbers?!?! Remaining: {data}")


o2 = find_number(init_data, keep_o2)
co2 = find_number(init_data, keep_co2)

print(int(o2, 2) * int(co2, 2))
