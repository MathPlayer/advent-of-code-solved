#!/usr/bin/env python3
""" Solving 11 advent 2019. """

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

LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3

DIRECTIONS = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}
TURN = {
    LEFT: {
        UP: LEFT,
        LEFT: DOWN,
        DOWN: RIGHT,
        RIGHT: UP
    },
    RIGHT: {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP
    }
}


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

    def run(self):
        """ Run as many steps as possible. """
        while not self.halted and not self.need_input:
            self.run_step()


def solve(filename, initial_value):
    """ Solve day 11. """
    program = read(filename)

    robot = IntcodeComputer(program)
    paint_map = defaultdict(int)
    coords = (0, 0)
    direction = UP
    painting = True

    paint_map[coords] = initial_value
    while not robot.halted:
        # Let it run wild.
        robot.inputs.append(paint_map[coords])
        robot.need_input = False
        robot.run()
        while robot.outputs:
            output = robot.outputs.pop(0)

            # Paint.
            if painting:
                paint_map[coords] = output
                painting = False
                continue

            # Move robot.
            if not painting:
                direction = TURN[output][direction]
                coords = (coords[0] + DIRECTIONS[direction][0],
                          coords[1] + DIRECTIONS[direction][1])
                painting = True

    print(len(paint_map))

    # For part 2 we should paint the map:
    if initial_value == 1:
        min_x = min(filter(lambda x: x[1] == 1, paint_map.items()), key=lambda x: x[0][0])[0][0]
        min_y = min(filter(lambda x: x[1] == 1, paint_map.items()), key=lambda x: x[0][1])[0][1]
        max_x = max(filter(lambda x: x[1] == 1, paint_map.items()), key=lambda x: x[0][0])[0][0]
        max_y = max(filter(lambda x: x[1] == 1, paint_map.items()), key=lambda x: x[0][1])[0][1]

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                print('#' if paint_map[(x, y)] == 1 else ' ', end='')
            print()


if __name__ == "__main__":
    solve("11.in", 0)
    solve("11.in", 1)
