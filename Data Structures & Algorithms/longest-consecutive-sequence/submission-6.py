class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 0 
        numset = set(nums)

        for n in nums:
            if (n-1) not in numset:
                # start of seq
                length =0 

                while (n + length ) in numset:
                    length += 1
                longestSeq = max(length, longestSeq) 
        return longestSeq