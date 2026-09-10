class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max = -1
        for i in range(n-1, -1, -1):
            print(f'i: {i}, arr[i]: {arr[i]}, max: {max}')
            old = arr[i]
            arr[i] = max
            max = old if old > max else max
        return arr