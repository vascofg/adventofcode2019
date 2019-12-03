import math


def compute(codes, pos=0):
    opcode = codes[pos]
    if opcode == 1:
        codes[codes[pos+3]] = codes[codes[pos+1]] + codes[codes[pos+2]]
    elif opcode == 2:
        codes[codes[pos+3]] = codes[codes[pos+1]] * codes[codes[pos+2]]
    elif opcode == 99:
        return codes
    else:
        raise Exception('Invalid opcode {} at position {}'.format(opcode, pos))

    return compute(codes, pos + 4)


if __name__ == '__main__':
    with open('./day2/input.txt') as file:
        codes = [int(code) for code in file.readline().split(',')]
    codes[1] = 12
    codes[2] = 2
    computed = compute(codes)
    print(computed[0])
    #incomplete, missing step 2