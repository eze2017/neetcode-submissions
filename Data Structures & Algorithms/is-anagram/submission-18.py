from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1_dict = Counter(s)
        s2_dict = Counter(t)
        print(s1_dict)

        return s1_dict == s2_dict
        
