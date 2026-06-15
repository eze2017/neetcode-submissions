class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_counter = {}
        has_dupe = False
        for item in nums:
            if item in dict_counter:
                dict_counter[item]+=1 
            else:
                dict_counter[item]= 1
        #print(dict_counter)
        for k,v in dict_counter.items():
            #print(k,v)
            if v > 1:
                has_dupe = True
        return has_dupe

