class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input nums = [3,4,5,6], target = 7
        # Output: [0,1]

        diff_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_map:
                return [diff_map[diff],i]
            
            diff_map[nums[i]]=i
        