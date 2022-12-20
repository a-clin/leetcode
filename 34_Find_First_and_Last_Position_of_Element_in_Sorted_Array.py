class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        if len(nums) == 0: return [-1, -1]
        n = len(nums)
        l, r = 0, n #[l, r)

        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target: 
                r = m
            else:
                l = m + 1
       
        if l == n or nums[l] != target : return [-1, -1]
        
        left = l
        r = n

        while l < r:
            m = l + (r-l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
                
        return [left, l-1]