class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_data = {}
        seen = False
        for item in nums:
            if item not in dict_data:
                dict_data[item] = False
                
            else:
                dict_data[item] = True
                seen = True

        return seen