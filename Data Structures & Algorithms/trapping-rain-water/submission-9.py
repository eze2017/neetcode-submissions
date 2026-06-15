class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        l = 0 
        r = len(height)-1
        Lmax = height[l]
        Rmax = height[r]

        while l < r :
            if Lmax < Rmax:
                l +=1
                Lmax = max(Lmax,height[l])
                res += Lmax -height[l]
            
            else:
                r -= 1
                Rmax = max(Rmax, height[r])
                res +=  Rmax - height[r]
        return res
