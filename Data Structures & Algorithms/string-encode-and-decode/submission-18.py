class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s =""
        for s in strs:
            new_s+=str(len(s))+'#'+s
        
        return new_s

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        
        res = []
        while i <len(s) :
            j = i
            while s[j] !='#':
                j+=1
       
            length = int(s[i:j])
            print(length)
            i = j+1
            j= i+length
            word=s[i:j]
            res.append(word)
            # print(i)
            # print(j)
            i = j
            
        return res


            

            
           
            
            
