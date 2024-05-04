import random
def findKthLargest(nums, k: int) -> int:
    #Quickselect
    k = len(nums) - k
    def quickselect(l, r):
        swapIndex, pivotIndex = l, random.randint(l,r)
        pivot = nums[pivotIndex]
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                swapIndex += 1
        nums[pivotIndex], nums[swapIndex] = nums[swapIndex], nums[pivotIndex]
        if swapIndex < k:
            return quickselect(swapIndex+1,r)
        elif swapIndex > k:
            return quickselect(l,swapIndex-1)
        else:
            return nums[swapIndex]
    return quickselect(0,len(nums)-1)

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))