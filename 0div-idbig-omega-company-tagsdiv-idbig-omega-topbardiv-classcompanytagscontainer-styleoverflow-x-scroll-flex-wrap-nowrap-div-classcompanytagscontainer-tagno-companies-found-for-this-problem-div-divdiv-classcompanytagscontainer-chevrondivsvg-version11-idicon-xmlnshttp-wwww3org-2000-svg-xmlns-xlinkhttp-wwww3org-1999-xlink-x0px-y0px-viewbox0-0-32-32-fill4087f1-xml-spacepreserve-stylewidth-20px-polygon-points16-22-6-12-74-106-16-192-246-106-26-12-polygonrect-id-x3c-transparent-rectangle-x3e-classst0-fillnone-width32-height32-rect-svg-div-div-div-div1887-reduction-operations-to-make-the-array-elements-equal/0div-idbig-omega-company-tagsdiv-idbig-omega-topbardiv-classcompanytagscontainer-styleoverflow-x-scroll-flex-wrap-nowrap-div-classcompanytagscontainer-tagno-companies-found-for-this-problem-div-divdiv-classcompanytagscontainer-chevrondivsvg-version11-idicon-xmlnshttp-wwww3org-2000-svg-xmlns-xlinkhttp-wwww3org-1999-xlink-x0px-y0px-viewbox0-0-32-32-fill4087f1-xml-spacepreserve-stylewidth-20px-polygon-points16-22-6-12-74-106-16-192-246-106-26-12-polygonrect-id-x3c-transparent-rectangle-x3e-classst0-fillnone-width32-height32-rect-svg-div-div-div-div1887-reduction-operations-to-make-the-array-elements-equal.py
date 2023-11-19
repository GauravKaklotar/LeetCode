class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        keys = list(counter.keys())
        keys.sort()
        for i in range(len(keys)):
            ans += (i * counter[keys[i]])
        
        return ans