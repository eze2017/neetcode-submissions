class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) -1 
        MaxLeft = height[l]
        MaxRight = height[r]
        res = 0 

        while l < r:
            if MaxLeft < MaxRight:
                l+= 1
                MaxLeft = max(MaxLeft,height[l])
                res += MaxLeft - height[l]
            
            else:
                r -= 1
                MaxRight = max(MaxRight,height[r])
                res += MaxRight-height[r]
        return res

