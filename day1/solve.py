import math
from functools import reduce


def fuel(mass):
    return mass//3-2


def realfuel(mass, sum=0):
    f = fuel(mass)
    if f <= 0:
        return sum
    return realfuel(f, sum + f)


def do_sum(x1, x2): return x1 + x2


if __name__ == '__main__':
    with open('./day1/input.txt') as file:
        masses = file.readlines()
    fuels = [fuel(int(x)) for x in masses]
    realFuels = [realfuel(int(x)) for x in masses]
    print(sum(fuels))
    print(sum(realFuels))
