class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2

        countOfThree, rem = divmod(n, 3)

        if rem == 0:
            return 3 ** countOfThree
        elif rem == 1:
            return 3 ** (countOfThree - 1) * 4
        else:
            return 3 ** countOfThree * 2 