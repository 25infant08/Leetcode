class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 30
        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    cnt[i] += 1
        ans = 0
        for _ in range(k):
            num = 0
            for i in range(30):
                if cnt[i]:
                    num |= 1 << i
                    cnt[i] -= 1
            ans = (ans + num * num) % mod
        return ans