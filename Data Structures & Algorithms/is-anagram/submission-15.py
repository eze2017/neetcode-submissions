class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def counter(s):
            counter_dict = collections.defaultdict(int)
            for c in s:
                if c in counter_dict:
                    counter_dict[c] +=1 
                else:
                     counter_dict[c] =1 

            return counter_dict

        s_anagram = counter(s)
        t_anagram = counter(t)

        if s_anagram == t_anagram:
            return True
        else:
            return False