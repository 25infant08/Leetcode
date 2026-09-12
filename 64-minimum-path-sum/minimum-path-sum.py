class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [float("inf")] * (n + 1)
        dp[1] = 0
        for row in grid:
            for j in range(1, n + 1):
                dp[j] = min(dp[j], dp[j - 1]) + row[j - 1]
        return dp[n]