class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                counter[i]+=1
        
        #print(type(counter.values()))

        print(counter)
        count_data = sorted(counter.items(),key=lambda x:x[1] ,reverse=True)
        # Extract the top k elements (keys)
        top_k = [item[0] for item in count_data[0:k] ]
        print(top_k)
        return top_k