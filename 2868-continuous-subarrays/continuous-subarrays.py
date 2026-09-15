from typing import List
from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_q = deque()
        min_q = deque()
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            while max_q and nums[max_q[-1]] <= x:
                max_q.pop()
            max_q.append(right)
            while min_q and nums[min_q[-1]] >= x:
                min_q.pop()
            min_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                if max_q[0] == left:
                    max_q.popleft()
                if min_q[0] == left:
                    min_q.popleft()
                left += 1
            ans += right - left + 1
        return ans