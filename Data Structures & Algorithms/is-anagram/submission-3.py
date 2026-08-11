class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            chars = [0] * 26
            for i, c in enumerate(s):
                chars[(ord(c) - ord("a"))] += 1
                chars[(ord(t[i]) - ord("a"))] -= 1
            return all(x==0 for x in chars)