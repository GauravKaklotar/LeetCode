class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow, onesCol, zerosRow, zerosCol = [0 for _ in range(len(grid))], [0 for _ in range(len(grid[0]))], [0 for _ in range(len(grid))], [0 for _ in range(len(grid[0]))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        return grid