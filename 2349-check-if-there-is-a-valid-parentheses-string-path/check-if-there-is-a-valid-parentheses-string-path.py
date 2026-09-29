class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 or grid[0][0] == ')':
            return False
        dp = [set() for _ in range(n)]
        dp[0].add(1)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                possible = set()
                if i > 0:
                    possible |= dp[j]
                if j > 0:
                    possible |= dp[j - 1]
                change = 1 if grid[i][j] == '(' else -1
                dp[j] = {
                    balance + change
                    for balance in possible
                    if balance + change >= 0
                }
        return 0 in dp[n - 1]