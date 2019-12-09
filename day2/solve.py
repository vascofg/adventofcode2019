import math


def compute(program, pointer=0):
    opcode = program[pointer]
    if opcode == 1:
        program[program[pointer+3]] = program[program[pointer+1]] + \
            program[program[pointer+2]]
    elif opcode == 2:
        program[program[pointer+3]] = program[program[pointer+1]] * \
            program[program[pointer+2]]
    elif opcode == 99:
        return program
    else:
        raise Exception(
            'Invalid opcode {} at position {}'.format(opcode, pointer))

    return compute(program, pointer + 4)


def setInputs(program, inputs):
    (noun, verb) = inputs
    newProgram = program.copy()
    newProgram[1] = noun
    newProgram[2] = verb
    return newProgram


if __name__ == '__main__':
    with open('./day2/input.txt') as file:
        program = [int(i) for i in file.readline().split(',')]
    inputs = (1, 12)
    computed = compute(setInputs(program, inputs))
    print(computed[0])

    desiredOutput = 19690720
    inputsGenerator = ((noun, verb) for noun in range(100) for verb in range(100))
    noun, verb = next(i for i in inputsGenerator if compute(
        setInputs(program, i))[0] == desiredOutput)
    print(100*noun+verb)
