from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))
        for i in range(1, len(word1) + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, len(word2) + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(prev, dp[j], dp[j - 1])
                prev = temp
        return dp[-1]