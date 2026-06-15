class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        
        sorted_dict = sorted(dict.items(),key=lambda x:x[1], reverse = True )
        res = [item[0] for item in sorted_dict[:k]]
        return res

