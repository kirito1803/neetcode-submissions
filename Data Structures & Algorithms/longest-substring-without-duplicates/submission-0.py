class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        start = 0
        ans = 0

        for end in range(len(s)):
            c = s[end]

            if c in last and last[c] >= start:
                start = last[c] + 1

            last[c] = end
            ans = max(ans, end - start + 1)

        return ans