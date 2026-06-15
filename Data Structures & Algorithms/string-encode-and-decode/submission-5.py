class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s = ""
        for s in strs:
            new_s += str(len(s))+'#'+s
        return new_s

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0 
        # 4#neet4#code4#love3#you

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            #print(s[i:j])
            length = int(s[i:j])
            i = j+1 
            j = i+length
            res.append(s[i:j])
            i =  j
        return res

            # print(length)
            # i+=1
            # j+=1
            
