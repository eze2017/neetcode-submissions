class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_dict = defaultdict(int)

        for n in nums:
            if n in counter_dict:
                counter_dict[n]+= 1

            else:
                counter_dict[n] = 1

        print(counter_dict)
        sorted_counter = sorted(counter_dict.items(),key = lambda  x:x[1] ,reverse = True)
        # top_k = [item[0] for item in sorted_items[:k]]
        top_k = [item[0] for item in sorted_counter[:k]]
        print(top_k)
        return top_k