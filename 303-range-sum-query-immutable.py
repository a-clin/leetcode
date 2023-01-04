class NumArray:

    def __init__(self, nums: List[int]): 
        self.sumList = [0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.sumList.append(sum)


    def sumRange(self, left: int, right: int) -> int:
        return self.sumList[right+1] - self.sumList[left]
        