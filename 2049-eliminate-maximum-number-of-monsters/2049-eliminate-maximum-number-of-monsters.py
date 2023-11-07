class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsterArrivals = sorted( [dist[i] / speed[i] for i in range(len(dist))])
        for i, monster in enumerate(monsterArrivals):
            if i >= monster: return i
        return i+1