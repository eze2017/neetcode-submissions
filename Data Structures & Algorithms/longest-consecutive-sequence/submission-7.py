class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: nums = [2,20,4,10,3,4,5]

        # Output: 4

       numset = set(nums)
       longest_seq = 0 

       for n in nums:
            if (n-1) not in numset:
                #start of seq
                length = 0 
                while (n+length) in nums:
                    length+=1
                    longest_seq = max(longest_seq, length)
       return longest_seq
