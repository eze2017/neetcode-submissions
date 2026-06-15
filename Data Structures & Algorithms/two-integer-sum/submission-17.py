class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_diff = {}
        for i , n in enumerate(nums):
            print(i,n)
            diff = target - n 
            if diff in dict_diff:
                return [dict_diff[diff],i]
            else:
                dict_diff[n]=i
        return []