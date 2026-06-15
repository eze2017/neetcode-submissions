class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
        dict_data= {}
        for i in nums:
            if i in dict_data:
                dict_data[i] += 1
            else:
                dict_data[i] =1
        
        for k,v in dict_data.items():
            if v > 1:
                return True
        return False
        

