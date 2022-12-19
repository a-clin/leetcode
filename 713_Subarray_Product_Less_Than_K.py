class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 : return 0
        left = ans = 0
        prod = 1

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            
            # add length of subarray
            # In example 1, the found subarrays are 
            # [10], [10, 5], [5, 2], [5, 2, 6]
            # the ans = 1+2+2+3
            ans += right - left + 1

        return ans