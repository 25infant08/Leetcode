class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        x = 1
        while x in s:
            x <<= 1
        return x