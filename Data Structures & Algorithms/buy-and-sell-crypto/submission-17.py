class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0 
        minbuy= prices[0]
        for sell in prices:
            minbuy = min(minbuy,sell)
            maxp = max(maxp, sell-minbuy)
        return maxp
