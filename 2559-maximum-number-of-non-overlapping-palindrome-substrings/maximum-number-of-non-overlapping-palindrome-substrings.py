class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if length <= 2:
                    pal[l][r] = s[l] == s[r]
                else:
                    pal[l][r] = s[l] == s[r] and pal[l + 1][r - 1]
        dp = [0] * (n + 1)
        for r in range(n):
            dp[r + 1] = dp[r]
            for l in range(r - k + 2):
                if r - l + 1 >= k and pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)
        return dp[n]