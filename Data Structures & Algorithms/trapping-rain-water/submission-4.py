class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        premax = height[0]
        suffix = [0] * n
        sufmax = height[n-1]
        total = 0

        for i, h in enumerate(height):
            if i == 0:
                prefix[i] = h
                continue
            prefix[i] = premax
            premax = h if h > premax else premax

        for i in range(n-1, 0, -1):
            if i == n-1:
                suffix[i] = sufmax
                continue
            suffix[i]=sufmax
            sufmax = height[i] if height[i] > sufmax else sufmax
        
        # print(prefix)
        # print(suffix)
        for i, h in enumerate(height):
            water = min(prefix[i], suffix[i]) - h
            water = 0 if water < 0 else water
            total += water
            # print(water) 
        return total