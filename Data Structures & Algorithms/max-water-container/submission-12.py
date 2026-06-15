class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: height = [1,7,2,5,4,7,3,6]
        # Output: 36

        l = 0 
        r = len(heights)-1
        max_area = 0 
        while l  < r :
            area = (r-l)*min(heights[l],heights[r])
            max_area=max(max_area,area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
           
        return max_area
