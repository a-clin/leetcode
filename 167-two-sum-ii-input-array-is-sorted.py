class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1

        while i < j:
            expect = target - nums[i]
            if expect == nums[j]:
                return [i+1, j+1]
            elif nums[j] > expect:
                j -= 1
            else:
                i += 1