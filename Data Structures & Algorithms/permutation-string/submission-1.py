class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if length of s1 is longer  return false
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 'a' to 'z'
        s1Count = [0]* 26
        s2Count = [0]* 26
        # build a Frequency of s1 and first window of s2 
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0 
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0 )
        
        # Left pointer of the sliding window
        l = 0 

        # Right pointer starts at end of first window
        for r in range(len(s1),len(s2)):
            # If all 26 chars match, we found a permutation
            if matches == 26: return True
            
            # ---- ADD right character ----
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # If it just became equal, we gained a match
            if s2Count[index] == s1Count[index]:
                matches += 1
            # If it was equal and now exceeded, we lost a match
            if s2Count[index] == s1Count[index]+1:
                matches -= 1
            
            # ---- REMOVE left character ----
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # If it just became equal, we gained a match
            if s2Count[index] == s1Count[index]:
                matches+= 1
            # If it was equal and now dropped below, we lost a match
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            # Move window forward
            l +=1 

        # Final window check
        return matches == 26
