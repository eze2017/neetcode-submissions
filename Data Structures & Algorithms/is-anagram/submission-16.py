class Solution:

    def dict_counter(self, s):
        dict_counter = defaultdict(int)
        for c in s:
            if c in dict_counter:
                dict_counter[c] +=1 
            else:
                dict_counter[c] =1
        return dict_counter




    def isAnagram(self, s: str, t: str) -> bool:

        dict1 = self.dict_counter(s)
        dict2 = self.dict_counter(t)

        return  dict1 == dict2
    


    