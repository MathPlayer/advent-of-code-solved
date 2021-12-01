input = open('input.txt', 'r').read().strip()
# input = open('input-test.txt', 'r').read().strip()

ints = [int(str.strip(x)) for x in input.split()]

result = 0
current_sum = None
for a, b, c in zip(ints, ints[1:], ints[2:]):
    new_sum = a + b + c
    if current_sum and current_sum < new_sum:
        result += 1
    current_sum = new_sum
print("Result: {}".format(result))
