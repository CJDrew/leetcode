def findTargetSumWays(nums, target: int) -> int:
    #Lets do it as a dfs first then add memoization to speed things up
    #Axis of cache are all positive and all negative
    cache = [[0] * len(nums) for i in range(len(nums))]
    def dfs(curSum, posSum, negSum):
        #Success case / out of bounds case
        if posSum + negSum == len(nums):
            return 1 if curSum == target else 0
        #Check to see if we hit something in the cache. If we did then we know there's a path
        #from here and we can just increment by one?
        if cache[posSum][negSum] != 0:
            return cache[posSum][negSum]
        #We haven't reached the end yet so keep going
        else:
            pos = dfs(curSum + nums[posSum + negSum], posSum+1, negSum)
            neg = dfs(curSum - nums[posSum + negSum], posSum, negSum+1)
            ans = pos + neg
            cache[posSum][negSum] = ans
            return ans

    return dfs(0, 0, 0)

print(findTargetSumWays([1,1,1,1,1], 3))