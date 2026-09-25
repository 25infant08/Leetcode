class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = -prices[0]
        sold = 0
        cooldown = 0
        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown
            hold = max(prev_hold, prev_cooldown - price)
            sold = prev_hold + price
            cooldown = max(prev_cooldown, prev_sold)
        return max(sold, cooldown)