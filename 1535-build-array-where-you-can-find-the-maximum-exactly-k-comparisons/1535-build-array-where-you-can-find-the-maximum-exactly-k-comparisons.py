"""
Here we are going to target this problem via dynamic programming and memoization, so let's understand what
exactly is required for it.

The `search_cost` is: assuming the first element is an increase from 1, how many "increase from max" do we have.

Thus, if n == 1, k ==1 is acceptable.

"""
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD_VAL = 10**9 + 7
        @cache
        def helper(n, m, k, max_so_far):
            # - (2) now the base cases.
            if n == 0:
                if k == 0:
                    return 1
                else:
                    return 0

            # - (1) let's first take care of the recursion
            number_of_ways = 0
            for j in range(1, m+1):
                if j <= max_so_far:
                    number_of_ways += helper(n-1, m, k, max_so_far) % MOD_VAL
                else:
                    number_of_ways += helper(n-1, m, k-1, j) % MOD_VAL

            return number_of_ways % MOD_VAL

        number_of_ways = 0
        for j in range(1, m+1):
            number_of_ways += helper(n-1, m, k-1, j) % MOD_VAL

        return number_of_ways % MOD_VAL
        