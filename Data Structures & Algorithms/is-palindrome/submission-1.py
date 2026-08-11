class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        l = len(s)
        n = l // 2
        for i in range(n):
            if s[i] != s[l - 1 - i]:
                return False
        return True