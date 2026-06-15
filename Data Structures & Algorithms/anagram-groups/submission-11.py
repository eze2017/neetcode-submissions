class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict= defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            group_dict[sortedS].append(s)
            print(group_dict)
        return list(group_dict.values())