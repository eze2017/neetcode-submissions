class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0 

        for sell in prices:
            buy = min(sell,buy)
            maxp= max(maxp, sell-buy)
        return maxp