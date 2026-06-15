class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
         # Frequency arrays for 'a' to 'z'
        s1Count = [0]*26 
        s2Count = [0]*26 
        # build a Frequency of s1 and first window of s2 
        for c in range(len(s1)):
           s1Count[ord(s1[c])-ord('a')] +=1
           s2Count[ord(s2[c])-ord('a')] +=1
        print(s1Count,s2Count)
        matches = 0 
        for i in range(26):
            matches+= (1 if s1Count[i]==s2Count[i] else 0 )
        print(matches)
        # left pointer of sliding window 
        l = 0 
        # Right pointer starts at end of first window
        for r in range(len(s1),len(s2)):
            # if all 26 permutations found return True 
            if matches ==26:
                return True
            
            # ---- ADD right char 
            index = ord(s2[r])-ord('a')
            s2Count[index]+=1
            # If it just became equal, we gained a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal and now exceeded, we lost a match
            if s1Count[index]+1 == s2Count[index]:
                matches -= 1
            # ---- Remove Left char 
            index = ord(s2[l])-ord('a')
            s2Count[index]-=1
            # If it just became equal, we gained a match
            if s1Count[index] == s2Count[index] :
                matches += 1
            # If it was equal and now we dropped, we lost a match
            if s1Count[index]-1 == s2Count[index]:
                matches -= 1
            l+=1
        return matches ==26


