def quicksort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    #recursive case
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        arr.pop(mid)
        less = [i for i in arr if i <= pivot]
        more = [i for i in arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)


print(quicksort([2,3,5,1,7,4]))