class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Input: numbers = [1,2,3,4], Output: [1,2] target = 3
        l = 0 
        r = len(numbers)-1
       
        
        while l < r:
            curr_target = numbers[l]+numbers[r]
            if curr_target > target:
                r -=1
            elif curr_target < target:
                l +=1
            elif curr_target ==target:
                return [l+1,r+1]
        return[]