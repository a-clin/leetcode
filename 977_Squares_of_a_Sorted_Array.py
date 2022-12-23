class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j, k = 0, len(nums)-1, len(nums)-1
        output = [0] * len(nums)

        while i <= j:
            if (abs(nums[i]) >= abs(nums[j])):
                output[k] = nums[i] ** 2
                i += 1
            else:
                output[k] = nums[j] ** 2
                j -= 1
            k -= 1
        
        return output