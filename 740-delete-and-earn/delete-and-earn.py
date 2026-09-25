class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        total = [0] * (max(nums) + 1)
        for num in nums:
            total[num] += num
        prev = curr = 0
        for value in total:
            prev, curr = curr, max(curr, prev + value)
        return curr