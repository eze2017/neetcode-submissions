class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_dupe = False
        duplicates= {}
        for item in nums:
            if item  not in duplicates:
                duplicates[item] = 1
            else:
                duplicates[item]+= 1
        
        for k,v in duplicates.items():
            if v >1:
                is_dupe = True
        return is_dupe
        