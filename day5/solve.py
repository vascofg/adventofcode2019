import math
import sys


def compute(program, input, pointer=0):
    digits = [digit for digit in str(program[pointer]).zfill(5)]
    opcode = int(''.join(digits[-2:]))
    modes = [int(mode) for mode in reversed(digits[:3])]

    # returns the value at the position if in position mode, otherwise returns the value directly
    def value(n): return program[program[pointer+n]
                                 ] if modes[n - 1] == 0 else program[pointer+n]

    if opcode == 1:
        program[program[pointer+3]] = value(1) + \
            value(2)
        pointer = pointer + 4
    elif opcode == 2:
        program[program[pointer+3]] = value(1) * \
            value(2)
        pointer = pointer + 4
    elif opcode == 3:
        program[program[pointer+1]] = input
        pointer = pointer + 2
    elif opcode == 4:
        print(value(1))
        pointer = pointer + 2
    elif opcode == 5:
        if(value(1) != 0):
            pointer = value(2)
        else:
            pointer = pointer + 3
    elif opcode == 6:
        if(value(1) == 0):
            pointer = value(2)
        else:
            pointer = pointer + 3
    elif opcode == 7:
        if(value(1) < value(2)):
            program[program[pointer+3]] = 1
        else:
            program[program[pointer+3]] = 0
        pointer = pointer + 4
    elif opcode == 8:
        if(value(1) == value(2)):
            program[program[pointer+3]] = 1
        else:
            program[program[pointer+3]] = 0
        pointer = pointer + 4
    elif opcode == 99:
        return program
    else:
        raise Exception(
            'Invalid opcode {} at position {}'.format(opcode, pointer))

    return compute(program, input, pointer)


if __name__ == '__main__':
    with open('./day5/input.txt') as file:
        program = [int(i) for i in file.readline().split(',')]
    print("----TEST 1 OUTPUT----")
    compute(program.copy(), 1)
    print("----TEST 2 OUTPUT----")
    compute(program.copy(), 5)
