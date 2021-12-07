# filename = 'input-test.txt'
filename = 'input.txt'
numbers = [int(x) for x in open(filename, 'r').read().strip().split(',')]

min_fuel = max(numbers) * max(numbers) * len(numbers) + 1
for x in range(min(numbers), max(numbers) + 1):
    s = 0
    for n in numbers:
        if n < x:
            diff = x - n
        else:
            diff = n - x
        if diff < 1:
            s += diff
        else:
            s += diff * (diff + 1) // 2
    min_fuel = min(min_fuel, s)

print(f"{min_fuel=}")
