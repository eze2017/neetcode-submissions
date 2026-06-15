class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            while s[r] in charset: # go through every char in set
                charset.remove(s[l]) # remove duplicate 
                l += 1    # increament by 1
            charset.add(s[r]) # add char to set
            res = max(res, r-l +1)
        return res
