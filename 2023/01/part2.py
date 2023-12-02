filename = 'input'
# filename = 'test'
data = open(filename).read()

sum = 0
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for entry in data.splitlines():
    first, last = None, None
    for i, c in enumerate(entry):
        if c.isdigit():
            if not first:
                first = int(c)
            last = int(c)
        else:
            for j, digit in enumerate(digits):
                if entry[i:].startswith(digit):
                    if not first:
                        first = j
                    last = j

    if first and last:
        print(f"{entry} adding {first} {last}")
        sum += first * 10 + last

print(sum)
