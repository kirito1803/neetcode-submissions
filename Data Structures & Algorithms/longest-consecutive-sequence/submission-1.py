class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlength = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                maxlength = length if (length > maxlength) else maxlength
        
        return maxlength