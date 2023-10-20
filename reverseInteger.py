def reverse(self, x: int) -> int:
        #Check for overflows
        minInt, maxInt = (-2 ** 31), (2 ** 31)-1
        if x <= minInt + 650000000 or x >= maxInt - 650000000:
            return 0

        #Preserve sign and add it back at the end
        sign = 1 if x >= 0 else -1
        x = abs(x)

        #Loop through each digit and construct a new number
        length = len(str(x))
        ans = 0
        i = 0
        while x > 0:
            num = x%10
            ans += num * (10 ** (length-i-1))
            x = x // 10
            i += 1
        
        return ans * sign

print(reverse(321))