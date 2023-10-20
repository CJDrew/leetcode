def intToRoman(num):       
        symbols = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        vals = sorted(list(symbols.keys()))[::-1]

        ans = []
        i = 0
        while num > 0:
            curVal = vals[i]
            while num > curVal:
                num -= curVal
                ans.append(symbols[curVal])
            i += 1
        return ans

intToRoman(5)