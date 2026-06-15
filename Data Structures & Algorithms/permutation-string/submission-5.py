class Solution:
   
    def checkInclusion(self,s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Step 1: Build frequency map for s1
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        # Step 2: Sliding window
        window_count = {}
        left = 0

        for right in range(len(s2)):
            # Add current character to window
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # If window size exceeds s1 length, shrink from left
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1

            # Step 3: Compare dictionaries
            if window_count == s1_count:
                return True

        return False