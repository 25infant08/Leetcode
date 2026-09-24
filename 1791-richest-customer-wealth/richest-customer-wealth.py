class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum = 0
        for account in accounts:
            maximum = max(maximum, sum(account))
        return maximum