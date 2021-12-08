filename = 'input-test.txt'
filename = 'input-test2.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

parsed = []
for line in lines:
    s = line.split('|')
    parsed.append((s[0].split(), s[1].split()))

ones = 0
fours = 0
sevens = 0
eights = 0
for signals, digits in parsed:
    for digit in digits:
        if len(digit) == 2:
            ones += 1
        if len(digit) == 4:
            fours += 1
        if len(digit) == 3:
            sevens += 1
        if len(digit) == 7:
            eights += 1

print(f"{ones=} {fours=} {sevens=} {eights=}")
print(f"{ones+fours+sevens+eights}")
