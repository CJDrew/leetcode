def longestPalindrome(s: str) -> str:
        ans = ""
        def expandPalindrome(i):
            ret = ""
            l = (i // 2) - 1 if i % 2 == 1 else (i//2)
            r = (i // 2) + 1 if i %2 == 1 else (i//2)
            while l <= 0 and r < len(s) and s[l] == s[r]:
                if l == r:
                    ret += s[l]
                else:
                    ret = s[l] + ret + s[r]
                l -= 1
                r += 1
            return ret
        
        for i in range(2 * len(s)):
            p = expandPalindrome(i)
            if len(p) > len(ans):
                ans = p
        return ans

print(longestPalindrome("babad"))