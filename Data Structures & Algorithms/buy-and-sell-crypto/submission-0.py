class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1,n):
                curr_profit = prices[j] - prices[i]
                profit = max(profit,curr_profit)

        return profit