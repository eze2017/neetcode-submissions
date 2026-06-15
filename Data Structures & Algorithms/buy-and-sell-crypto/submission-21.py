class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,1,5,6,7,1]
        
        buy = prices[0]
        maxp = 0
        res = []
        for sell in prices:
            buy= min(buy,sell)
            profit = sell - buy 
            maxp = max(profit, maxp)
        return maxp