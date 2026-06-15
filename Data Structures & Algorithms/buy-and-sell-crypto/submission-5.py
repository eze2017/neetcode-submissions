class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxP = 0
        # [10,1,5,6,7,1]
        while r < len(prices):
            # check if profitable 
            if prices[l] < prices [r]:
                profit = prices[r] - prices[l]
                maxP = max(profit,maxP)
            else:
                l = r
            r += 1
        return maxP