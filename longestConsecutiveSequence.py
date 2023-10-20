def longestConsecutive(nums) -> int:
    ans = 0
    nums = set(nums)
    visited = {}
    for n in nums:
        if n not in visited:
            visited[n] = 1
            nextNum = n + 1
            cur = 1
            while nextNum in nums:
                if nextNum in visited:
                    cur = cur + visited[nextNum]
                    visited[nextNum-1] = cur
                    break
                else:
                    cur += 1
                    visited[nextNum] = cur
                    nextNum += 1
            ans = max(ans, cur)
    return ans

print(longestConsecutive([0,1,-1]))