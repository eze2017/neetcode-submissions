class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force 

        s1 = sorted(s)
        s2 = sorted(t)

        return s1== s2