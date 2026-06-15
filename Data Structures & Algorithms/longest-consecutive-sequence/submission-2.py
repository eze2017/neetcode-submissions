class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        numset = set(nums)
        print(numset)
        seq = 0

        for num in numset:
            if (num -1) not in numset:
                length = 1
                while(num+length) in numset:
                    length += 1
                seq = max(length, seq)
        return seq
