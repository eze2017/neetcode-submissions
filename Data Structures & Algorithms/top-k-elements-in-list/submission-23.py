class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        heap = []
        dict_freq=Counter(nums)
        for key,value in dict_freq.items():
            if len(heap) < k or value > heap[0][0]:
                heapq.heappush(heap,[value,key])
                print(heap)
            if len(heap)>k:
                heapq.heappop(heap)
        return [item[1] for item in heap]
                
