from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_count = Counter(nums)
        heap = []
        # nums=[1,2,2,3,3,3]
        # k =2
        # {3: 3, 2: 2, 1: 1}
        for key ,value in freq_count.items():
            if len(heap) < k or value > heap[0][0]:
                heapq.heappush(heap,[value,key])
            if len(heap) >k:
                heapq.heappop(heap)
        
        print(heap)
        return [ n[1] for n in heap]

