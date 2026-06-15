class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = 0 
        r = 1
        nums.sort()
        while l < r and r <len(nums) :
            if nums[l] == nums[r]:
                return True
            else:
                l+= 1
                r+= 1
        return False