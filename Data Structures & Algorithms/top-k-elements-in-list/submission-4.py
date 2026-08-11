import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        topk = []

        for num, freq in counts.items():
            heapq.heappush(topk, (freq, num))

            if len(topk) > k:
                heapq.heappop(topk)

        return [num for freq, num in topk]