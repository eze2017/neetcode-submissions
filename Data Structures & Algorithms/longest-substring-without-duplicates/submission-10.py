class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        res = 0 
        l = 0 

        for r in range(len(s)):
            ## continous check 
            while s[r] in charset:
                # remove s[l] to keep non dupes
                charset.remove(s[l])
                # move l poitner (make window small)
                l +=1 
            ## add unique
            charset.add(s[r])
            res = max(res,r-l+1)
        return res