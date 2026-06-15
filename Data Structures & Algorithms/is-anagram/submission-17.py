class Solution:
    
    def create_map(self , s):
        counter = {}
        for c in s:
            if c in counter:
                counter[c]+= 1
            else:
                counter[c]=1
        return counter

    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = self.create_map(s)
        t_dict = self.create_map(t)

        return s_dict == t_dict
