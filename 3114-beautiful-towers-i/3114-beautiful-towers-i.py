class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        N = len(maxHeights)
        if N == 1:
            return maxHeights[0]
        ans = 0
        for peak in range(N):
            res = maxHeights[peak]
            cur = maxHeights[peak]
            for i in range(peak-1, -1, -1):
                cur = min(cur, maxHeights[i])
                res += cur
            cur = maxHeights[peak]
            for i in range(peak+1, N):
                cur = min(cur, maxHeights[i])
                res += cur
            ans = max(ans, res)
        return ans