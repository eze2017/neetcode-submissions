class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res =0 
        l = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                # remove s[l] to keep non dupes
                charSet.remove(s[l])
                # move l poitner (make window small)
                l+= 1
            charSet.add(s[r])
            res = max(r-l+1, res)
        return res