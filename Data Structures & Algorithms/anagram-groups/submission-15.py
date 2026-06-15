class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            group_dict[sorted_s].append(s)
        return list(group_dict.values())