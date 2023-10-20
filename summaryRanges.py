def summaryRanges(nums):
    ans = []
    def addToList(num1, num2):
        if num1 == num2:
            ans.append(str(num1))
        else:
            ans.append(str(num1) + "->" + str(num2))


    a, b = 0, 0
    while b < len(nums)-1:
        last = nums[b]
        b += 1
        if nums[b] - last > 1:
            addToList(nums[a], last)
            a = b
    
    addToList(nums[a], nums[b])
    return ans

print(summaryRanges([0,1,2,4,5,7]))