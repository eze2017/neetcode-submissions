class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        is_dupe = False

        for item in nums:
            if item in counter:
                counter[item]+= 1
            else:
                counter[item]=1

        print(counter)

        for k,v in counter.items():
            print(k,v)
            if v >1 :
                is_dupe = True
        return is_dupe