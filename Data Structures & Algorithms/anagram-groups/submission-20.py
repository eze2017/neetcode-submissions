class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        group_dict=defaultdict(list)
        for word in strs:
            char_count = [0]*26
            for c in word:
                char_count[ord(c)-ord('a')]+=1
            group_dict[tuple(char_count)].append(word)
        print(group_dict)

        return list(group_dict.values())

