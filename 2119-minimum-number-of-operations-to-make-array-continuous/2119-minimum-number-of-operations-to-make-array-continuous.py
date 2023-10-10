class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        ans = sys.maxsize

        for i, start in enumerate(nums):
            end = start + n - 1
            index = bisect_right(nums, end)

            ans = min(ans, n - (index - i))
        return ans
            