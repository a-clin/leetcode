class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        
        while right < len(s): 
            while s[right] in s[left:right] and left < right:
                left += 1
            
            ans = max(ans, right-left+1)
            right += 1
        
        return ans
            