class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = defaultdict(list)
        for s in strs:
            counter = [0]*26
            for c in s:
                counter[ord(c)-ord('a')]+= 1
                print(counter)
            groups_dict[tuple(counter)].append(s)
        return list(groups_dict.values())
        