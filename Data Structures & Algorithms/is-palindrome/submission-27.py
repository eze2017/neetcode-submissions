class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Input: s = "Was it a car or a cat I saw?"

        # Output: true
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s+=c.lower()
        return new_s == new_s[::-1]
        
