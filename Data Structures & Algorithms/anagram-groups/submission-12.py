class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_dict = defaultdict(list)
        new_s = ""
        for s in strs:
         
           group_dict[new_s.join(sorted(s))].append(s)
        #print(group_dict)
        return list(group_dict.values())
