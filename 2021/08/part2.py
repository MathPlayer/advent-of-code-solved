from itertools import permutations


def ssort(string):
    return "".join(sorted(string))


filename = 'input-test.txt'
filename = 'input-test2.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

parsed = []
for line in lines:
    s = line.split('|')
    parsed.append((s[0].split(), s[1].split()))

segments = "abcdefg"
correct = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

result = 0
for i, (signals, digits) in enumerate(parsed):
    print(f"{i=}")
    encoding = {ssort(signal) for signal in signals}
    found = False
    for permutation in permutations(segments):
        translation = {x: y for (x, y) in zip(segments, permutation)}
        attempt = {
            ssort(translation[x] for x in string): i
            for string, i in correct.items()
        }
        if attempt.keys() == encoding:
            if found:
                raise Exception(f"Multiple translations for {(i, signals, digits)}")
            found = True
            line_result = 0
            for digit in map(ssort, digits):
                line_result = line_result * 10 + attempt[digit]
            result += line_result
    if not found:
        raise Exception(f"Cannot find translation for {(i, signals, digits)}")


print(f"{result=}")
