def calculate(s: str) -> int:
    i = 0
    s = s.replace(' ','')
    lastIndex = 
    #Do mult/div first
    while i < len(s):
        if s[i] in ['+','-']:
            lastIndex = i
        if s[i] in ['*','/']:
            end = i + 1
            while end < len(s):
                if s[end] in ['+','-','*','/']:
                    break
                end += 1
            num1 = int(s[lastIndex+1:i])
            num2 = int(s[i+1:end])
            if s[i] == '*':
                ans = num1*num2
            else:
                ans = num1//num2
            s = s[:lastIndex+1] + str(ans) + s[end:]
            i = 0
        else:
            i += 1
    
    #now do add/subtract
    i = 0
    while i < len(s):
        if s[i] in ['+','-'] and i != 0:
            #We don't need to backtrack for start since we always process the first op on the left
            start = 0
            end = i + 1
            while end < len(s):
                if s[end] in ['+','-']:
                    break
                end += 1
            num1 = int(s[start:i])
            num2 = int(s[i+1:end])
            if s[i] == '+':
                ans = num1+num2
            else:
                ans = num1-num2
            s = s[:start] + str(ans) + s[end:]
            i = 0
        else:
            i += 1
    return int(s)

print(calculate('3/2'))