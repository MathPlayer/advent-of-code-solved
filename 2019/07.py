#!/usr/bin/env python3
""" Solving 07 advent 2019. """

from itertools import permutations


def read(filename):
    """ read input data. """
    with open(filename) as input_file:
        file_data = [int(x) for x in input_file.read().strip().split(",")]

    return file_data


def run(software, phase, input_signal):
    """ Run the software using the phase and the input_signal. """

    i = 0
    inputs = [phase, input_signal]
    while True:
        opcode = software[i] % 100
        mode_1 = software[i] // 100 % 10
        mode_2 = software[i] // 1000 % 10
        # parameter_mode 0 - position, 1 - value
        if opcode == 99:
            break
        elif opcode == 1:
            # pos3 = pos1 + pos2
            p_1 = software[software[i + 1]] if mode_1 == 0 else software[i + 1]
            p_2 = software[software[i + 2]] if mode_2 == 0 else software[i + 2]
            software[software[i + 3]] = p_1 + p_2
            i += 4
        elif opcode == 2:
            # pos3 = pos1 * pos2
            p_1 = software[software[i + 1]] if mode_1 == 0 else software[i + 1]
            p_2 = software[software[i + 2]] if mode_2 == 0 else software[i + 2]
            software[software[i + 3]] = p_1 * p_2
            i += 4
        elif opcode == 3:
            # pos3 = input
            software[software[i + 1]] = inputs.pop(0)
            i += 2
        elif opcode == 4:
            # pos4 = output
            output = software[software[i + 1]]
            i += 2
        elif opcode == 5:
            p_1 = software[software[i + 1]] if mode_1 == 0 else software[i + 1]
            p_2 = software[software[i + 2]] if mode_2 == 0 else software[i + 2]
            if p_1 != 0:
                i = p_2
            else:
                i += 3
        elif opcode == 6:
            p_1 = software[software[i + 1]] if mode_1 == 0 else software[i + 1]
            p_2 = software[software[i + 2]] if mode_2 == 0 else software[i + 2]
            if p_1 == 0:
                i = p_2
            else:
                i += 3
        elif opcode == 7:
            p_1 = software[software[i + 1]] if mode_1 == 0 else software[i + 1]
            p_2 = software[software[i + 2]] if mode_2 == 0 else software[i + 2]
            software[software[i + 3]] = 1 if p_1 < p_2 else 0
            i += 4
        elif opcode == 8:
            p_1 = software[software[i + 1]] if mode_1 == 0 else software[i + 1]
            p_2 = software[software[i + 2]] if mode_2 == 0 else software[i + 2]
            software[software[i + 3]] = 1 if p_1 == p_2 else 0
            i += 4
        else:
            raise Exception("invalid opcode at index-ish: ", software[i:i+5])

    return output


class Amplifier:
    """ Class to keep track of one amplifier's ins/outs. """

    def __init__(self, amp_index, phase, ints):
        self.amp_index = amp_index
        self.ints = ints
        self.inputs = [phase]
        self.outputs = []
        self.i = 0
        self.halted = False
        self.need_input = False

    def run_step(self):
        """ Run one step of the operations. """
        # print(">>>", self.amp_index, self.ints)

        opcode = self.ints[self.i] % 100
        mode_1 = self.ints[self.i] // 100 % 10
        mode_2 = self.ints[self.i] // 1000 % 10
        # mode_3 = self.ints[i] // 10000
        # parameter_mode 0 - position, 1 - value
        if opcode == 99:
            self.halted = True
        if opcode == 1:
            # pos3 = pos1 + pos2
            p_1 = self.ints[self.ints[self.i + 1]] if mode_1 == 0 else self.ints[self.i + 1]
            p_2 = self.ints[self.ints[self.i + 2]] if mode_2 == 0 else self.ints[self.i + 2]
            self.ints[self.ints[self.i + 3]] = p_1 + p_2
            self.i += 4
        if opcode == 2:
            # pos3 = pos1 * pos2
            p_1 = self.ints[self.ints[self.i + 1]] if mode_1 == 0 else self.ints[self.i + 1]
            p_2 = self.ints[self.ints[self.i + 2]] if mode_2 == 0 else self.ints[self.i + 2]
            self.ints[self.ints[self.i + 3]] = p_1 * p_2
            self.i += 4
        if opcode == 3:
            # pos3 = input
            if not self.inputs:
                self.need_input = True
                return
            self.ints[self.ints[self.i + 1]] = self.inputs.pop(0)
            self.i += 2
        if opcode == 4:
            # Save output.
            self.outputs.append(self.ints[self.ints[self.i + 1]])
            self.i += 2
        if opcode == 5:
            p_1 = self.ints[self.ints[self.i + 1]] if mode_1 == 0 else self.ints[self.i + 1]
            p_2 = self.ints[self.ints[self.i + 2]] if mode_2 == 0 else self.ints[self.i + 2]
            self.i = p_2 if p_1 != 0 else self.i + 3
        if opcode == 6:
            p_1 = self.ints[self.ints[self.i + 1]] if mode_1 == 0 else self.ints[self.i + 1]
            p_2 = self.ints[self.ints[self.i + 2]] if mode_2 == 0 else self.ints[self.i + 2]
            self.i = p_2 if p_1 == 0 else self.i + 3
        if opcode == 7:
            p_1 = self.ints[self.ints[self.i + 1]] if mode_1 == 0 else self.ints[self.i + 1]
            p_2 = self.ints[self.ints[self.i + 2]] if mode_2 == 0 else self.ints[self.i + 2]
            self.ints[self.ints[self.i + 3]] = 1 if p_1 < p_2 else 0
            self.i += 4
        if opcode == 8:
            p_1 = self.ints[self.ints[self.i + 1]] if mode_1 == 0 else self.ints[self.i + 1]
            p_2 = self.ints[self.ints[self.i + 2]] if mode_2 == 0 else self.ints[self.i + 2]
            self.ints[self.ints[self.i + 3]] = 1 if p_1 == p_2 else 0
            self.i += 4
        # print("<<<", self.amp_index, self.ints)

    def run_until_input_needed_or_halt(self):
        """ Run as many steps as possible. """
        while not self.halted and not self.need_input:
            self.run_step()


def solve_1(filename):
    """ Solve day 08 part 1. """
    ints = read(filename)

    max_value = 0
    for permutation in permutations(range(5)):
        value = 0
        for i in permutation:
            value = run(ints.copy(), i, value)
        if max_value < value:
            print("New max value", value, "for", permutation)
            max_value = value


def solve_2(filename):
    """ Solve day 08 part 2. """
    ints = read(filename)

    max_value = 0
    for permutation in permutations([5, 6, 7, 8, 9]):
        amps = [Amplifier(x, permutation[x], ints.copy()) for x in range(5)]
        signals = [0]
        iteration = 0
        while True:
            # print("------------- Iteration", iteration)
            for amp in amps:
                amp.inputs += signals
                amp.need_input = False
                amp.run_until_input_needed_or_halt()
                signals = amp.outputs
                amp.outputs = []
            if amps[-1].halted:
                break
            iteration += 1

        # print(permutation, signals)
        if max_value < signals[-1]:
            print("New max value", signals[-1], "for", permutation)
            max_value = signals[-1]


if __name__ == "__main__":
    # solve_1("07-example-1.in")
    solve_1("07.in")
    print("------------------------------------")

    # solve_2("07-example-2.in")
    solve_2("07.in")
