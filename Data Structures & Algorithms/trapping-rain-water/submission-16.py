class Solution:
    def trap(self, height: List[int]) -> int:
        # Input: height = [0,2,0,3,1,0,1,3,2,1]

        # Output: 9

        l = 0 
        r = len(height)-1
        max_water = 0 
        maxL = height[l]
        maxR = height[r]

        while l < r :
            if height[l] < height[r]:
                maxL = max(maxL,height[l])
                max_water += maxL-height[l]
                l+=1
            else:
                maxR = max(maxR,height[r])
                max_water += maxR-height[r]
                r-=1
            
        return max_water





