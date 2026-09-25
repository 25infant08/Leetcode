class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = matrix[0][:]
        for i in range(1, len(matrix)):
            curr = []
            for j in range(len(matrix)):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j < len(matrix) - 1:
                    best = min(best, dp[j + 1])
                curr.append(matrix[i][j] + best)
            dp = curr
        return min(dp)