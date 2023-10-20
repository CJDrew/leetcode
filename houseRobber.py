def rob(nums) -> int:
    #Approach 1D dp array where each element represents the max value I could obtain up to that
    #point. One extra element for having robbed no houses
    dp = [0 for i in range(len(nums) + 1)]
    #Pad the nums array with an extra 0 to make my life easier
    nums = [0] + nums

    #Now iterate through each element. I can either skip the current house or take it and give up
    #The previous house
    for i in range(1,len(nums)):
        lastVal = dp[i-1]
        curVal = nums[i] if i < 2 else dp[i-2] + nums[i]
        dp[i] = max(lastVal, curVal)
    
    #Last value should be total possible value
    return dp[len(nums) - 1]

print(rob([1,2,3,1]))
