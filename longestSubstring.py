def longestSubstring(s):
    ans = 0
    seen = {}

    l, r = 0, 0
    
    while r < len(s):
        cur = s[r]
        if cur in seen and seen[cur] >= l:
            l = seen[cur]
        else:
            ans = max(ans, r - l + 1)
        seen[cur] = r
        r += 1
    return ans

print(longestSubstring("pwwkew"))