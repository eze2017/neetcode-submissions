class Solution:
    from typing import List
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for word in strs:
            char_list = [0]*26
            for c in word:
                char_list[ord('a')-ord(c)]+=1
           
            group_dict[tuple(char_list)].append(word)
        result = list(group_dict.values())
        return result

