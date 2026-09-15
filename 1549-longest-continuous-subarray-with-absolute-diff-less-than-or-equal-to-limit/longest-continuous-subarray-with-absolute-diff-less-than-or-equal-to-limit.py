from collections import deque
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()
        left = 0
        ans = 0
        for right in range(len(nums)):
            while minQ and nums[minQ[-1]] > nums[right]:
                minQ.pop()
            minQ.append(right)
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()
            maxQ.append(right)
            while nums[maxQ[0]] - nums[minQ[0]] > limit:
                if minQ[0] == left:
                    minQ.popleft()
                if maxQ[0] == left:
                    maxQ.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans