class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        print(target)
        print(nums)
        for i , n in enumerate(nums):
            diff = target - n
            if diff in diff_dict:
                return [diff_dict[diff],i]
            else:
                diff_dict[n]=i
            print(diff_dict)
        return []