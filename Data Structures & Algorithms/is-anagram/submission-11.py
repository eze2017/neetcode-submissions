class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def create_dict(data:str)->dict:
            char_freq={}
            for c in data:
                if c in char_freq:
                    char_freq[c]+=1
                else:
                    char_freq[c]=1
            return char_freq
        
        freq_s = create_dict(s)
        freq_t = create_dict(t)
        return freq_s == freq_t

            
                