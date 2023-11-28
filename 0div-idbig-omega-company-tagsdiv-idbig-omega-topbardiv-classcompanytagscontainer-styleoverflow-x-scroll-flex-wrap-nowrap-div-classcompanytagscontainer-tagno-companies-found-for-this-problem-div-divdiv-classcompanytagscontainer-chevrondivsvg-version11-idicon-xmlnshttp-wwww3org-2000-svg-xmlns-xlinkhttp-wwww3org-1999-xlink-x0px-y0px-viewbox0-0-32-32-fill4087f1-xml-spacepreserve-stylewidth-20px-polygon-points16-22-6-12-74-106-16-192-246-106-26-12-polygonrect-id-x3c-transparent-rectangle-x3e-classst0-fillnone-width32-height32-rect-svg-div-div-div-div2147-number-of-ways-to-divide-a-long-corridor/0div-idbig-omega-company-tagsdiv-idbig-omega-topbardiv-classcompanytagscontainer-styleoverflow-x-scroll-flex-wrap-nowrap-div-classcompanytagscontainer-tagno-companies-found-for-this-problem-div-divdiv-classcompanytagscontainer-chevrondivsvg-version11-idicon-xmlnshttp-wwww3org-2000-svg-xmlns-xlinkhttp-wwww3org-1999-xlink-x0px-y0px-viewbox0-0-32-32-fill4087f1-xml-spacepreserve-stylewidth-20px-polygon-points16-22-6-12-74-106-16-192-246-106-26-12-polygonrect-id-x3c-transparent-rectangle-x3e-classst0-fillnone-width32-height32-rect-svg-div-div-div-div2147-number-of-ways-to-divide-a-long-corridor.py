class Solution:
    def numberOfWays(self, corr: str) -> int:
        indeces = [i for i, c in enumerate(corr) if c == 'S']
        l = len(indeces)
        if l % 2 or l == 0:
            return 0

        ans = 1
        for i in range(1, l - 1, 2):
            ans *= indeces[i + 1] - indeces[i]

        return ans % (10**9+7)