class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s = ""
        for s in strs:
            new_s+= str(len(s))+'#'+s
        return new_s

    def decode(self, s: str) -> List[str]:

        res =[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
          # 5#Hello5#World
            length =int(s[i:j])
            print(length)
            i = j+1
            j = i + length
            word = s[i:j]
            print(word)
            res.append(word)
            i = j
          
        return res
            
          
            