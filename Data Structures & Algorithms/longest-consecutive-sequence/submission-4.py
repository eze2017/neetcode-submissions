class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0 

        for num in numset:
           if (num - 1) not in numset:
                seq = 1
                while (num + seq ) in numset:
                    seq += 1
                longest = max(seq,longest)
        return longest