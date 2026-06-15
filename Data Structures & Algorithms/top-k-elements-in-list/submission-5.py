class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        for item in nums:
            if  item in counter_dict:
                counter_dict[item] += 1
            else:
                counter_dict[item]= 1
        

        sorted_keys = sorted(counter_dict.items(),key = lambda x:x[1],reverse=True)
        res = [sorted_key[0] for sorted_key in sorted_keys[:k]]
        print(res)
        return res