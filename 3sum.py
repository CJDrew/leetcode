def threeSum(nums):
    #We don't need duplicate numbers
    ans = []
    #Make a list of compliments then try all combos to see if we can find one: O(N^2)
    compliments = set()
    for i in range(len(nums)):
        compliments.add(-1*nums[i])
    
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] in compliments:
                ans.append([nums[i], nums[j], -1 * (nums[i] + nums[j])])
    return ans

print(threeSum([-1,0,1,2,-1,-4])) 