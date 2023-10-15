class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
    
        @lru_cache(1000)
        def dp(pos = 0, stepsRem = steps)-> int:

            if (pos > stepsRem or                # too far to get back with steps remaining
                not 0 <= pos < arrLen):          # off the array
                return 0

            if pos == 0 == stepsRem:             # made it to zero
                return 1                         # with no steps left
                
            stepsRem-= 1                         # decrement step count

            return (dp(pos  , stepsRem) + dp(pos-1, stepsRem) + dp(pos+1, stepsRem))

        return dp() % (10**9 + 7)