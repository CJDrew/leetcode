def search(nums, target):
    #Can we just unpivot, search, then adjust the index for the pivot?

    #Find the pivot
    pivot = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            pivot = i
            break
    #Unpivot the array
    nums = nums[pivot:] + nums[:pivot]

    #Binary search
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            #Adjust for pivot
            if mid >= pivot:
                return mid - pivot
            else:
                return mid + (len(nums) - pivot)
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(search([4,5,6,7,0,1,2], 0))