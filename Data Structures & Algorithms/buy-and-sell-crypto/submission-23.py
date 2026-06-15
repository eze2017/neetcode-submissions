class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        l = 0 
        r = 1
        maxp=0
        # prices = [10,1,5,6,7,1]
        for r in range(len(prices)):
            # profitble
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                maxp= max(profit,maxp)
            else:
                l = r 
            r+=1
            
        return maxp
        

