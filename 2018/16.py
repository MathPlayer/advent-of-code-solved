#!/usr/bin/env python3


def addr(memory, a, b, c):
    memory[c] = memory[a] + memory[b]


def addi(memory, a, b, c):
    memory[c] = memory[a] + b


def mulr(memory, a, b, c):
    memory[c] = memory[a] * memory[b]


def muli(memory, a, b, c):
    memory[c] = memory[a] * b


def banr(memory, a, b, c):
    memory[c] = memory[a] & memory[b]


def bani(memory, a, b, c):
    memory[c] = memory[a] & b


def bonr(memory, a, b, c):
    memory[c] = memory[a] | memory[b]


def boni(memory, a, b, c):
    memory[c] = memory[a] | b


def setr(memory, a, b, c):
    memory[c] = memory[a]


def seti(memory, a, b, c):
    memory[c] = a


def gtir(memory, a, b, c):
    memory[c] = 1 if a > memory[b] else 0


def gtri(memory, a, b, c):
    memory[c] = 1 if memory[a] > b else 0


def gtrr(memory, a, b, c):
    memory[c] = 1 if memory[a] > memory[b] else 0


def eqir(memory, a, b, c):
    memory[c] = 1 if a == memory[b] else 0


def eqri(memory, a, b, c):
    memory[c] = 1 if memory[a] == b else 0


def eqrr(memory, a, b, c):
    memory[c] = 1 if memory[a] == memory[b] else 0


OPS = set([addr, addi, mulr, muli, banr, bani, bonr, boni, setr, seti,
           gtir, gtri, gtrr, eqir, eqri, eqrr])


def read_list(l, sep):
    return list(map(int, l.split(sep)))


##################################################################################################
# Read
with open("16.in") as f:
    lines = list(map(str.strip, f.readlines()))

# Get samples
samples = []
for i in range(0, len(lines), 4):
    if not lines[i].startswith("Before"):
        break
    before = read_list(lines[i][9:-1], ", ")
    data = read_list(lines[i + 1], " ")
    after = read_list(lines[i + 2][9:-1], ", ")
    samples.append([before, data, after])

# Get the rest
program = []
while i < len(lines):
    if lines[i]:
        line = read_list(lines[i], " ")
        program.append(line)
    i += 1

# Part 1
response = 0
for (b, d, a) in samples:
    count = 0
    for op in OPS:
        c = b.copy()
        op(c, d[1], d[2], d[3])
        if c == a:
            count += 1
        if count >= 3:
            break
    if count >= 3:
        response += 1
print(response)

# Part 2
guess = {op: set([k for k in range(16)]) for op in OPS}
for (b, d, a) in samples:
    for op in OPS:
        if len(guess[op]) == 1:
            continue
        c = b.copy()
        op(c, d[1], d[2], d[3])
        if c != a:
            guess[op].discard(d[0])

OPCODES = {}
while len(OPCODES) < 16:
    for op in OPS:
        if len(guess[op]) == 1:
            opcode = list(guess[op])[0]
            OPCODES[opcode] = op
            for op in OPS:
                guess[op].discard(opcode)
            break

registers = [0, 0, 0, 0]
for opcode, a, b, c in program:
    OPCODES[opcode](registers, a, b, c)
print(registers)
