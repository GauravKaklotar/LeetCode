class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()

        # if n==0: return False
        # if n==1: return True
        # return n%4==0 and self.isPowerOfFour(n/4)