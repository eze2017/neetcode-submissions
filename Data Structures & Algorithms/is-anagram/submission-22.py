class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        s1_dict = self.create_dict(s)
        s2_dict = self.create_dict(t)

        return s1_dict == s2_dict

    def create_dict(self,s:str):
        dictionary = {}
        for c in s:
            if c in dictionary:
                dictionary[c]+=1
            else:
                dictionary[c]=1
        return dictionary



