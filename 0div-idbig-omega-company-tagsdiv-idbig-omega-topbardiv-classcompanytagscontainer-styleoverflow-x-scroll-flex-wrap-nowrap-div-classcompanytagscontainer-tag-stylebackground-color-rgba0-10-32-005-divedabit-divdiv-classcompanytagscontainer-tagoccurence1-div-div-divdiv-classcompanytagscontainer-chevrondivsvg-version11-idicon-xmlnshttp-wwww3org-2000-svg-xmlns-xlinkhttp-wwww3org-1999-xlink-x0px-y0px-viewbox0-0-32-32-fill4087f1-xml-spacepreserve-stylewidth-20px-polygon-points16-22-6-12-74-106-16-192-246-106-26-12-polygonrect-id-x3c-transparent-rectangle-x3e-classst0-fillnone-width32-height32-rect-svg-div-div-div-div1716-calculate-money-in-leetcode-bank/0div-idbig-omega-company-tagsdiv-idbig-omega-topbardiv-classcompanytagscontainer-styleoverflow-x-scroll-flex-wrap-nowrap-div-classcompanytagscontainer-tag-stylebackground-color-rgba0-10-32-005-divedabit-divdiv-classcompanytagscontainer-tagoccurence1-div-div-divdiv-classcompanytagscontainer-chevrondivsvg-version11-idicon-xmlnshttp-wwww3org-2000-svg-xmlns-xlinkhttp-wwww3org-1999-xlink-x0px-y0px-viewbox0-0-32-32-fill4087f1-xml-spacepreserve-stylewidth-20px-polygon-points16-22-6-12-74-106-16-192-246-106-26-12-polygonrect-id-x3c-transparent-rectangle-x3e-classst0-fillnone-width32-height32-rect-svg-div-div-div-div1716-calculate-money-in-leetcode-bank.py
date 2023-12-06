class Solution:
    def totalMoney(self, n: int) -> int:
        d, r = divmod(n, 7)
        return d * (2 * 28 + 7 * (d - 1)) // 2 + r * (r + 1) // 2 + d * r