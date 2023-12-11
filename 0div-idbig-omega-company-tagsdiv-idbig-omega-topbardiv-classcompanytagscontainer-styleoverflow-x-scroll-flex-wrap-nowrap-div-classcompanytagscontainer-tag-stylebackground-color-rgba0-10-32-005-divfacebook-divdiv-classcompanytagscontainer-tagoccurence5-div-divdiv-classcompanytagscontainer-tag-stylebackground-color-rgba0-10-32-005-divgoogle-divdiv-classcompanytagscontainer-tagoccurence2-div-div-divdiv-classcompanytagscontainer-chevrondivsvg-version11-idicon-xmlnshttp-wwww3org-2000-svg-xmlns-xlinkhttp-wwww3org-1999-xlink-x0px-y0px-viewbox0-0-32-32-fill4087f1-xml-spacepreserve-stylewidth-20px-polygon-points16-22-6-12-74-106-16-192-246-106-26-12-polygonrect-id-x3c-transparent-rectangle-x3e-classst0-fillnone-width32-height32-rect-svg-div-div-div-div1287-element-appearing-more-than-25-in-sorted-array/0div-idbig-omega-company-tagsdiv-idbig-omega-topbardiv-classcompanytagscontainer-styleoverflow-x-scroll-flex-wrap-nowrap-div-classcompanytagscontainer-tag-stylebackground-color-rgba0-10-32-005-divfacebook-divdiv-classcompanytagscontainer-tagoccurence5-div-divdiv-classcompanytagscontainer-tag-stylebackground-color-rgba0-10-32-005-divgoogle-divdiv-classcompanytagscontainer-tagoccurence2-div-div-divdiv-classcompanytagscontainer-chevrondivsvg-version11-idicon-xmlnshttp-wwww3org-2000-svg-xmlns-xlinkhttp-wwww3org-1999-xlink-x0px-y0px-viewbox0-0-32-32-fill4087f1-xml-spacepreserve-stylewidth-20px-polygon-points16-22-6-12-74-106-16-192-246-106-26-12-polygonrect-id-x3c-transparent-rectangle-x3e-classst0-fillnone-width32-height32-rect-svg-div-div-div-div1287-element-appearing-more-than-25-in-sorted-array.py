class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for x in set(arr):
            if arr.count(x)/n > 0.25: return x