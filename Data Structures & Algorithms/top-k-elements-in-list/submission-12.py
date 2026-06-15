from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = Counter(nums)
        
        sorted_elements = sorted(element_count.items(),key=lambda x:x[1], reverse=True)
        print(sorted_elements)
        return [ n[0] for n in sorted_elements[:k]]
        