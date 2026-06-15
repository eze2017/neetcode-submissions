class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        is_dupe = False
        for item in nums:
            if item in data:
                 data[item] +=1
            else:
                data[item] =1
        
        for k,v in data.items():
            print(k,v)
            if v > 1:
                is_dupe = True
        return is_dupe
        
        