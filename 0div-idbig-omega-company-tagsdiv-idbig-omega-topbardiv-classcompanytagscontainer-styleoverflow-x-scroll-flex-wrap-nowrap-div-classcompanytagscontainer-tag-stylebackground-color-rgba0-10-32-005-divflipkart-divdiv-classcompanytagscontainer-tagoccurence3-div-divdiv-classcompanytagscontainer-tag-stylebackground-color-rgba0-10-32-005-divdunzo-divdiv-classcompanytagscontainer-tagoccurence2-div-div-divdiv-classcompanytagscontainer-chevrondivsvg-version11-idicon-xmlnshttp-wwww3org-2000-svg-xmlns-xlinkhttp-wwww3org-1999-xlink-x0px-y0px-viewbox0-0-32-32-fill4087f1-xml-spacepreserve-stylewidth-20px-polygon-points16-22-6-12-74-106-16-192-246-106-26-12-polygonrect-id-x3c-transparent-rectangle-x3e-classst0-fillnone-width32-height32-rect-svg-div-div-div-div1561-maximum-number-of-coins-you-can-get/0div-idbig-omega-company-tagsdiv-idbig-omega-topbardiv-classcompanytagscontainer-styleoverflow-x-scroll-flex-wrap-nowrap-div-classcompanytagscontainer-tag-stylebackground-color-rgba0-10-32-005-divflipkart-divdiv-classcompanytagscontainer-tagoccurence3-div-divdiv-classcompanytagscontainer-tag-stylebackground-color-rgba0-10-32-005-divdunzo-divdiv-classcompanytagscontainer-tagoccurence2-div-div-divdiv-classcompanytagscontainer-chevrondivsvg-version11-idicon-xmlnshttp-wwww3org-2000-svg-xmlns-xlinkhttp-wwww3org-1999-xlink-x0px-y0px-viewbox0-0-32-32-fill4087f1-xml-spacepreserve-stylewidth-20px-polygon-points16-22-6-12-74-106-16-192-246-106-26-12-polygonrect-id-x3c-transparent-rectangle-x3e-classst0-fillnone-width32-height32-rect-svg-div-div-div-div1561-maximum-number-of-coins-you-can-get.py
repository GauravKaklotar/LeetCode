class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        i, j = 0, len(piles)-1
        while i < j:
            ans += piles[i+1]
            j -= 1
            i += 2
        return ans