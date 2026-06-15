class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy = prices[0]
        # [10,1,5,6,7,1]

        for sell in prices:
            profit = max(profit,sell-buy)
            buy= min (buy, sell)
        return profit

