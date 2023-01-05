class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = set(candyType)
        return min(len(candy), int(len(candyType)/2))