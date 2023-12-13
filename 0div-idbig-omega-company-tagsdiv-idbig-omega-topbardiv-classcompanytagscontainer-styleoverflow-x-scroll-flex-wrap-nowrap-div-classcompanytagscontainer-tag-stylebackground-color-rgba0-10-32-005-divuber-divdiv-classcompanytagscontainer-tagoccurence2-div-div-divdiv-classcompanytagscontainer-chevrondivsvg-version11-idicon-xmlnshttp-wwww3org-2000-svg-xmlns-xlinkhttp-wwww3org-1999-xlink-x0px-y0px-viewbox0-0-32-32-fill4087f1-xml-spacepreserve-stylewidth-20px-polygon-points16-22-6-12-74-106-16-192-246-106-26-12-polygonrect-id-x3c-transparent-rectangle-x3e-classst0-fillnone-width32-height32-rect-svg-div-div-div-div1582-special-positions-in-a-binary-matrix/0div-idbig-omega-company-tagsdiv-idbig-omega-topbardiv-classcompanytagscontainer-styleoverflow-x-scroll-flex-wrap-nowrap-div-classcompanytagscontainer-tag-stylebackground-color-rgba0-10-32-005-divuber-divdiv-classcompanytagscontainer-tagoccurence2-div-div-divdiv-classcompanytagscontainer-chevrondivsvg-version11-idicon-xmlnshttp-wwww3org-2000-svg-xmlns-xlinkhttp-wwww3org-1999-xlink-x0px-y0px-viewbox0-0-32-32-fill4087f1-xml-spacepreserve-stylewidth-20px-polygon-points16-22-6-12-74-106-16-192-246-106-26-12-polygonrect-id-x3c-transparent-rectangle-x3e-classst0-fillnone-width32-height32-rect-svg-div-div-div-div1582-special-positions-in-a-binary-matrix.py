class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0

        # Lists to store the sums of elements in each row and column
        row_sums = [0] * len(mat)
        col_sums = [0] * len(mat[0])

        # Calculate the sums of elements in each row and column
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                row_sums[i] += mat[i][j]
                col_sums[j] += mat[i][j]

        # Check if each 1 is special using the precalculated sums
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    result += 1

        return result