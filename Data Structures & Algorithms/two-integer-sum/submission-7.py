class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_diff = {} # value--> index
        for i in range(len(nums)):
            print(nums[i],i)
            diff = target - nums[i]
            if diff in dict_diff:
                #print(dict_diff[diff])
                return [dict_diff[diff],i]
            else:
                dict_diff[nums[i]] = i




        