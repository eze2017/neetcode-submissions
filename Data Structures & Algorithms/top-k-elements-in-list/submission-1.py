class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = defaultdict(int)
        for num in nums:
            frequency_count[num] += 1

        #print(frequency_count)
        frequency_list = []
        
        for key,value in frequency_count.items():
            #print(k,v)
            if len(frequency_list) < k or value > frequency_list[0][0]:
               heapq.heappush(frequency_list,[value,key])
            if len(frequency_list) > k:
                heapq.heappop(frequency_list)

        return [ i[1] for i in frequency_list ]