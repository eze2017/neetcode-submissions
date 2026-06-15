class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_S = ""
        for c in s:
            if c.isalnum():
                new_S += c.lower()
        return new_S == new_S[::-1]
