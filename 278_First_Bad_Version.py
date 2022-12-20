# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n+1
        while l < r: 
            m = l + (r - l) //2
            if isBadVersion(m) == False:
                l = m+1
            else:
                r = m
        return r
