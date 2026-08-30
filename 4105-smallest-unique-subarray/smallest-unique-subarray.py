from typing import List
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        MOD1 = 1_000_000_007
        MOD2 = 1_000_000_009
        BASE = 911382323
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i, x in enumerate(nums):
            x += 1
            h1[i + 1] = (h1[i] * BASE + x) % MOD1
            h2[i + 1] = (h2[i] * BASE + x) % MOD2
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = pow1[i - 1] * BASE % MOD1
            pow2[i] = pow2[i - 1] * BASE % MOD2
        def check(length: int) -> bool:
            count = {}
            p1 = pow1[length]
            p2 = pow2[length]
            for i in range(n - length + 1):
                j = i + length
                x1 = (h1[j] - h1[i] * p1) % MOD1
                x2 = (h2[j] - h2[i] * p2) % MOD2
                key = (x1, x2)
                count[key] = count.get(key, 0) + 1
            return any(v == 1 for v in count.values())
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left