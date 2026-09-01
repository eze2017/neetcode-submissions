class Solution:
    from collections import Counter

    def isAnagram(self, s: str, t: str) -> bool:
        
        def create_dict(s):
            dict_data ={}

            for c in s:
                if c in dict_data:
                    dict_data[c]+=1
                else:
                    dict_data[c]=1
            return dict_data
        
        s_count = create_dict(s)
        print(s_count)
        t_count = create_dict(t)
        print(t_count)
        return s_count == t_count


            