class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i , n in enumerate(nums):
            print(i,n)
            differnce = target - n
            print(differnce)
            if differnce in diff_dict:
                return [diff_dict[differnce],i]
            diff_dict[n]=i
