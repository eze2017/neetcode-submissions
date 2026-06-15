class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 0 
        numset = set(nums)

        for n in nums: # for every item in  
            # check if it has left neighbour n -1 
            if (n-1) not in numset:
                length = 1  # start of sequence 
                while (n+length) in numset:
                    length += 1
                longestSeq = max(longestSeq, length)
        return longestSeq