class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float: 
        if poured == 0: return 0

        tower = [0.0] * 102
        tower[0] = poured

        for i in range(query_row):
            temp = [0.0] * 102

            for j in range(i+1):
                overflow = max(0, (tower[j]-1.0)/2.0)
                temp[j] += overflow
                temp[j+1] += overflow
            
            tower = temp
        return min(1.0, tower[query_glass])