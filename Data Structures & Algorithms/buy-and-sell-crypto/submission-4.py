class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for price in prices:
            buy = min(price,buy)
            maxProfit = max(maxProfit,price-buy)
        return maxProfit
            