def minCostClimbingStairs(cost) -> int:
    #Approach 2D dp.
    dp = [0 for i in range(len(cost))]
    for i in range(2,len(dp)):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[-1], dp[-2])

print(minCostClimbingStairs([1,100,1,1,100,1]))