class Solution:
    def searchInsert(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > val:
                r = m
            elif nums[m] == val:
                r = m
            elif nums[m] < val:
                l = m+1
        
        return l