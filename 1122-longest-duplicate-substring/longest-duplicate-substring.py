class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        MOD1 = 1_000_000_007
        MOD2 = 1_000_000_009
        BASE = 911382323
        nums = [ord(c) - ord('a') + 1 for c in s]
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        for i in range(n):
            h1[i + 1] = (h1[i] * BASE + nums[i]) % MOD1
            h2[i + 1] = (h2[i] * BASE + nums[i]) % MOD2
            p1[i + 1] = (p1[i] * BASE) % MOD1
            p2[i + 1] = (p2[i] * BASE) % MOD2
        def get_hash(l, r):
            x1 = (h1[r] - h1[l] * p1[r - l]) % MOD1
            x2 = (h2[r] - h2[l] * p2[r - l]) % MOD2
            return (x1, x2)
        def check(length):
            seen = {}
            for i in range(n - length + 1):
                key = get_hash(i, i + length)
                if key in seen:
                    j = seen[key]
                    if s[i:i + length] == s[j:j + length]:
                        return i
                seen[key] = i
            return -1
        left, right = 1, n - 1
        best_start = -1
        best_len = 0
        while left <= right:
            mid = (left + right) // 2
            start = check(mid)
            if start != -1:
                best_start = start
                best_len = mid
                left = mid + 1
            else:
                right = mid - 1
        if best_start == -1:
            return ""
        return s[best_start:best_start + best_len]