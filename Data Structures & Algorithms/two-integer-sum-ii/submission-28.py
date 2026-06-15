class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Input: numbers = [1,2,3,4], target = 3
        # Output: [1,2]

        l = 0 
        r = len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]


