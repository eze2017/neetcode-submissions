class Solution:
    
   

    def isAnagram(self, s: str, t: str) -> bool:
        
        def create_dict(data:str):
            char_freq = {}
            for c in data:
                if c in char_freq:
                    char_freq[c] += 1
                else:
                    char_freq[c] = 1
            return char_freq

        # if len(s) != len(t):
        #     return False
        
        freq_s = create_dict(s)
        freq_t = create_dict(t)
        print(freq_s)
        print(freq_t)
        return freq_t == freq_s