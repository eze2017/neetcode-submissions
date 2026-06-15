class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0 , len(nums)-1
        #index = -1
        while l <= r: 
            middle = (l+r ) //2
            if target == nums[middle]:
                return middle 
            # left sorted portion
            if nums[l] <= nums[middle]:
                if target >=nums[l] and target < nums[middle]:
                    r  = middle - 1
                else:
                    l = middle + 1
            else: 
                nums[r] >= nums[middle]
                if target > nums[middle] and target <= nums[r]:
                    l  = middle + 1
                else:
                    r = middle -1
        return -1
        
        
            





