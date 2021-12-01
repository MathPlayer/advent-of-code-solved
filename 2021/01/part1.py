input = open('input.txt', 'r').read().strip()
# input = open('input-test.txt', 'r').read().strip()

ints = [int(str.strip(x)) for x in input.split()]

result = 0
for a, b in zip(ints, ints[1:]):
    if a < b:
        result += 1
print("Result: {}".format(result))
