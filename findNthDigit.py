def findNthDigit(n: int) -> int:
    curDigits = 1
    curNumber = 9

    while n >= curDigits * curNumber:
        n -= curDigits * curNumber
        curDigits += 1
        curNumber *= 10

    place = n % (curDigits) - 1
    number = (curNumber // 10) + (n // curDigits) + 1
    return int(str(number)[place])

print(findNthDigit(10))