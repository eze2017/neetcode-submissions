class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        #print(freq_count)
        for n in nums:
            if n in freq_count:
                freq_count[n] += 1
            else:
                freq_count[n] =1
        
        print(freq_count)
        sorted_freq = sorted(freq_count.items(),key = lambda x:x[1], reverse = True)
        print(sorted_freq)
        # find top K 
        topK = [item[0] for item in sorted_freq[:k]]
        print(topK)
        return topK