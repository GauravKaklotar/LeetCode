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

"""
Approach
Why 3s? By testing various numbers, it becomes evident that the number 3 plays a significant role in maximizing the product. For example:

4 = 2 + 2 (product = 4)
5 = 2 + 3 (product = 6)
6 = 3 + 3 (product = 9)
7 = 3 + 2 + 2 (product = 12)
8 = 3 + 3 + 2 (product = 18)
9 = 3 + 3 + 3 (product = 27)
Why not 4s? Anytime we have a 4, we can always split it into two 2s, which will give a better or equal product.

Handling Remainders: When n is divided by 3, the remainder can be 0, 1, or 2:

Remainder 0: n is a perfect multiple of 3. We break n entirely into 3s.
Remainder 1: It's better to take a 3 out and add a 4 (which is split as two 2s). This is because the product of three numbers, 3, 1, and n-4, is less than the product of the two numbers, 4 and n-4.
Remainder 2: We simply multiply the leftover 2 with the product of all 3s.
Complexity
Time complexity: O(log n). This is because our primary operation involves raising 3 to the power of count_of_3s which, in Python, takes O(log n) time.

Space complexity: O(1). We only use a constant amount of extra space regardless of the input size.
"""