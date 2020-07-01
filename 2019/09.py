#!/usr/bin/env python3
""" Solving 09 advent 2019. """

from collections import defaultdict

def read(filename):
    """ read input data. """
    with open(filename) as input_file:
        file_data = [int(x) for x in input_file.read().strip().split(",")]

    return defaultdict(lambda: 0, {index: value for (index, value) in enumerate(file_data)})

HALT = 99
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
RELATIVE = 9


class IntcodeComputer:
    """ Class to be reused as IntcodeComputer. """

    def __init__(self, program):
        self.program = program
        self.inputs = []
        self.outputs = []
        self.index = 0
        self.halted = False
        self.need_input = False
        self.relative_base = 0

    def print_program(self, tag=""):
        """ Prints the program. """
        to_print = []
        for (_, program_value) in sorted(self.program.items()):
            to_print.append(program_value)
        print(tag, self.index, to_print)

    def get(self, offset, mode):
        """ Gets the value for the given mode, using index and offset."""
        # parameter_mode 0 - position, 1 - value, 2 - relative
        index = self.index + offset
        if mode == 0:
            return self.program[self.program[self.index + offset]]
        if mode == 1:
            return self.program[self.index + offset]
        if mode == 2:
            return self.program[self.program[self.index + offset] + self.relative_base]
        raise Exception("Invalid get for mode", mode)

    def set(self, offset, mode, value):
        """ Sets the value at index + offset. Increments the index by offset + 1. """
        if mode == 0:
            self.program[self.program[self.index + offset]] = value
        elif mode == 2:
            self.program[self.program[self.index + offset] + self.relative_base] = value
        else:
            raise Exception("Invalid set for mode", mode)
        self.index += offset + 1

    def parse_op(self):
        """ Returns (opcode, mode_1, mode_2) for value at i. """
        return (self.program[self.index] % 100,
                self.program[self.index] // 100 % 10,
                self.program[self.index] // 1000 % 10,
                self.program[self.index] // 10000)

    def run_step(self):
        """ Run one step of the operations. """
        opcode, mode_1, mode_2, mode_3 = self.parse_op()
        p_1 = self.get(1, mode_1)
        p_2 = self.get(2, mode_2)
        if opcode == HALT:
            self.halted = True
        if opcode == ADD:
            self.set(3, mode_3, p_1 + p_2)
        if opcode == MULTIPLY:
            self.set(3, mode_3, p_1 * p_2)
        if opcode == INPUT:
            if not self.inputs:
                self.need_input = True
                return
            self.set(1, mode_1, self.inputs.pop(0))
        if opcode == OUTPUT:
            self.outputs.append(p_1)
            self.index += 2
        if opcode == JUMP_IF_TRUE:
            self.index = p_2 if p_1 != 0 else self.index + 3
        if opcode == JUMP_IF_FALSE:
            self.index = p_2 if p_1 == 0 else self.index + 3
        if opcode == LESS_THAN:
            self.set(3, mode_3, 1 if p_1 < p_2 else 0)
        if opcode == EQUALS:
            self.set(3, mode_3, 1 if p_1 == p_2 else 0)
        if opcode == RELATIVE:
            self.relative_base += p_1
            self.index += 2

    def run(self, new_inputs=[]):
        """ Run as many steps as possible. """
        self.inputs += new_inputs
        while not self.halted and not self.need_input:
            self.run_step()


def solve_1(filename):
    """ Solve day 08 part 1. """
    program = read(filename)

    computer = IntcodeComputer(program)
    computer.run([1])
    print(computer.outputs)

def solve_2(filename):
    """ Solve day 08 part 1. """
    program = read(filename)

    computer = IntcodeComputer(program)
    computer.run([2])
    print(computer.outputs)


if __name__ == "__main__":
    solve_1("09-example-0.in")
    solve_1("09-example-1.in")
    solve_1("09-example-2.in")
    solve_1("09.in")
    solve_2("09.in")
