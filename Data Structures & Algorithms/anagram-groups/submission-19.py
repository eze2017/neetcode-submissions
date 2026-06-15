class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = defaultdict(list)
        for s in strs:
            char_count = [0]*26
            for c in s:
                char_count[ord(c)-ord('a')]+=1
            groups_dict[tuple(char_count)].append(s)
        
        return list(groups_dict.values())

        