class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_seq = 0 

        for n in nums:
            if not (n-1) in numset:
                # start of sequence 
                seq = 0 

                while (n+seq) in numset:
                    seq+=1 
                    longest_seq = max(longest_seq, seq)
        return longest_seq