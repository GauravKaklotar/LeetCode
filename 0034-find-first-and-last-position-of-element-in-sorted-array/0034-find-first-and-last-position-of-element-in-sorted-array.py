import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0; end = len(nums)
        def left_bound():
            left = start; right = end
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left if left < len(nums) and nums[left] == target else -1

        def right_bound():
            left = start; right = end
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left - 1 if left - 1 >= 0 and nums[left - 1] == target else -1
        first_pos = left_bound()
        second_pos = right_bound()
        return [first_pos,second_pos]
        