from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        element_count = defaultdict(int)
        for n in nums:
            element_count[n]+=1
        
        for key,value in element_count.items():
            if len(heap) < k or value > heap[0][0]:
                heapq.heappush(heap,[value,key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n[1] for n in heap]


        