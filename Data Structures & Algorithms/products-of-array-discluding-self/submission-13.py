class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        print(res)
        prefix = 1
        for i in range(len(res)):
            res[i] = prefix
            prefix *= nums[i]
            
        
        #print(prefix)
        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        print(res)
        return res