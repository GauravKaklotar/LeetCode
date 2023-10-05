class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = floor(len(nums) / 3)
        counter = Counter(nums)

        ans = []
        for key, val in counter.items():
            if val > x: ans.append(key)
        return ans