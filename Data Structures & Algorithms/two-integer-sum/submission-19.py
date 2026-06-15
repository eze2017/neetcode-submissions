class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, n in enumerate(nums):
            print(i, n)
            diff = target - n
            print(diff)
            if diff in target_dict:
                return [target_dict[diff],i]
            
            target_dict[n] = i
        return []
            
      