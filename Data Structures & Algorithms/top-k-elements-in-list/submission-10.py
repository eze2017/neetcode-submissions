class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            if n in counter:
                counter[n] +=1
            else:
                counter[n] =1

        #print(counter)
        sorted_counter = sorted(counter.items(),key= lambda x:x[1],reverse=True)
        #print(sorted_counter)
        res = [item[0] for item in sorted_counter[:k]]
        print(res)
        return res