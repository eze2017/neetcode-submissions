class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_counter = defaultdict(int)
        for n in nums:
            if n in k_counter:
                k_counter[n] += 1
            else:
                k_counter[n] =1 
        print(k_counter)
        sorted_items = sorted(k_counter.items(),key = lambda x:x[1],reverse = True )
        print(sorted_items)
        # Extract the top k elements (keys)
        topk = [item[0] for item in sorted_items[:k]]
        print(topk)
        return topk