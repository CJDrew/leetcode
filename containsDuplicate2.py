def containsNearbyDuplicate(nums, k):
        cur = set(nums[0:k+2])
        a, b = 0, k+1

        if len(cur) < k + 1:
            return True
        
        while b < len(nums):
            #b in cur
            cur.remove(nums[a])
            a += 1
            cur.add(nums[b])
            b += 1
        
        return False

containsNearbyDuplicate([1,2,3,1,9,9,9], 3)