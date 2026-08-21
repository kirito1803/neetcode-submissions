class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxUnits = 0
        l,r = 0, len(heights)-1
        while l != r:
            units =  (r-l) * min(heights[l], heights[r])
            maxUnits = units if units > maxUnits else maxUnits
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return maxUnits