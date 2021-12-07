# filename = 'input-test.txt'
filename = 'input.txt'
numbers = [int(x) for x in open(filename, 'r').read().strip().split(',')]

min_fuel = max(numbers) * len(numbers) + 1
for x in range(min(numbers), max(numbers) + 1):
    s = 0
    for n in numbers:
        if n < x:
            s += x - n
        else:
            s += n - x
    min_fuel = min(min_fuel, s)

print(f"{min_fuel=}")
