def jump(nums):
    #Approach: 1D dp array where each cell represents the minimum number of jumps required
    #to reach the end. Last spot is 0 since it's the end
    dp = [len(nums) for i in range(len(nums))]
    dp[len(nums) - 1] = 0

    #Iterate through dp array backwards and solve each sub problem
    for i in range(len(nums) - 2, -1, -1):
        #If this jump would carry us to the end
        if nums[i] + i >= len(nums) - 1:
            dp[i] = 1
        #Otherwise it should be 1 + min number of jumps from where we land
        else:
            dp[i] = 1 + dp[nums[i] + i]
    
    return dp[0]

print(jump([2,3,0,1,4]))