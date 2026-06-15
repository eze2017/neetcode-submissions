class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s =""
        for s in strs:
            new_s += str(len(s))+'#'+s
        print(new_s)
        return new_s


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != '#':
                j+=1
            # hit # 
            length = int(s[i:j])
            i = j+ 1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j 
        return res



        