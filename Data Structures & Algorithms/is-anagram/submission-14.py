class Solution:

    def create_counter(self,s):
            counter = defaultdict()
            for c in s:
                if c in counter:
                   counter[c] += 1
                else:
                    counter[c] =1 
            return counter


    def isAnagram(self, s: str, t: str) -> bool:
        
        str_t = self.create_counter(t)

        str_s  = self.create_counter(s)

        return str_t == str_s
