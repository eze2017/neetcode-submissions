from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1_chars = Counter(s)
        dict2_chars = Counter(t)
      
        # for k,v in dict1_chars.items():
        #     print(k,v)
        #     if not dict2_chars[k]:
        #         return False
        #     elif dict2_chars[k] != v:
        #         return False
        # return True
        return dict1_chars == dict2_chars