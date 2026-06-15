class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l =0 
        r = n-1

        while l < r :
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l +1 ,r+1]
            if summ > target:
                r -= 1
            if summ < target :
                l += 1
        
        # for i in range(n):
        #     current_sum = numbers[i]+ numbers[r]
        #     print(current_sum)
        #     print(l)
        #     print(r)
        #     if current_sum > target :
        #         r -= 1
        #     if current_sum < target:
        #         l += 1 
        #     if target == current_sum:
        #         return [numbers[l],numbers[r]] 
          