def convertToTitle(columnNumber: int) -> str:
    #Approach: convert base 10 to base 26
    base = 26
    asciiOffset = 64
    ans = ""
    while columnNumber:
        charNum = columnNumber % base if columnNumber != 26 else 26
        cur = chr(charNum + asciiOffset)
        ans = cur + ans
        columnNumber = columnNumber // base
    return ans

print(convertToTitle(701))