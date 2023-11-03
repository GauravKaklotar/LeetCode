class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return [
            x
            for i in range(1, target[-1] + 1)
            for x in ["Push"] + ["Pop"] * (i not in set(target))
        ]