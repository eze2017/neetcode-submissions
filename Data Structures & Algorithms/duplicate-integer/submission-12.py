class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_dict ={}
        for n in nums:
            if n in dupe_dict:
                return True
            else:
                dupe_dict[n]=1
        return False
        