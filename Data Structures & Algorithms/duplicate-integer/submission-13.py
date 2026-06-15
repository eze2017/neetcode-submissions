class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counter_dict = Counter(nums)
        for k ,v in counter_dict.items():
            if v >1 :
                return True
        return False