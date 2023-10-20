
class NumArray:

    def __init__(self, nums):
        self.sums = []
        curSum = 0
        for num in nums:
            curSum += num
            self.sums.append(curSum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[max(0,left-1)]
    

test = NumArray([-2,0,3,-5,2,-1])
test.sumRange(0,2)