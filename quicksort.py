# def quicksort(arr):
#     #base case
#     if len(arr) <= 1:
#         return arr
#     #recursive case
#     else:
#         mid = len(arr) // 2
#         pivot = arr[mid]
#         arr.pop(mid)
#         less = [i for i in arr if i <= pivot]
#         more = [i for i in arr if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(more)
nums = [2,3,5,1,7,4]

def quicksort(l,r):
    pivot = r
    swapIndex = l
    for i in range(l,r+1):
        if i == pivot:
            continue
        if nums[i] <= nums[pivot]:
            nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
            swapIndex += 1
    nums[pivot], nums[swapIndex] = nums[swapIndex], nums[pivot]
    quicksort(l, swapIndex)
    quicksort(swapIndex+1,r)

print(quicksort(0,5))