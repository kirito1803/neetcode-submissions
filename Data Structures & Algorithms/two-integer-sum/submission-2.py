class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            different = target - nums[i]

            if different in seen:
                return [seen[different], i]

            seen[nums[i]] = i