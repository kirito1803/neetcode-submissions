class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for string in strs:
            counts = [0]*26
            for c in string:
                counts[ord(c)-ord("a")] += 1
            key = tuple(counts)
            groups.setdefault(key, []).append(string)
        
        return list(groups.values())