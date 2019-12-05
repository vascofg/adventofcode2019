PW_LENGTH = 6


def validLength(digits):
    return len(digits) == PW_LENGTH


def doubleDigits(digits):
    return any(
        digits[i] == digits[i+1]
        for i in range(len(digits) - 1)
    )


def increasingDigits(digits):
    return all(
        digits[i] <= digits[i+1]
        for i in range(len(digits) - 1)
    )


def isValidPassword(password):
    digits = [int(d) for d in password]
    return validLength(digits) and doubleDigits(digits) and increasingDigits(digits)


def onlyDoubleDigits(digits):
    current = None
    count = i = 0
    while i in range(len(digits)):
        digit = digits[i]
        nextDigit = digits[i+1] if i<len(digits)-1 else None
        if(digit == current):
            count = count + 1
        else:
            current = digit
            count = 1
        if(count == 2 and nextDigit != digit):
            return True
        
        i = i+1
    return False

def isValidPassword2(password):
    digits = [int(d) for d in password]
    return validLength(digits) and onlyDoubleDigits(digits) and increasingDigits(digits)


if __name__ == '__main__':
    with open('./day4/input.txt') as file:
        start, end = [int(r) for r in file.readline().split('-')]
    print(
        len(
            [pw for pw in range(start, end) if isValidPassword(str(pw))]
        )
    )
    print(
        len(
            [pw for pw in range(start, end) if isValidPassword2(str(pw))]
        )
    )
