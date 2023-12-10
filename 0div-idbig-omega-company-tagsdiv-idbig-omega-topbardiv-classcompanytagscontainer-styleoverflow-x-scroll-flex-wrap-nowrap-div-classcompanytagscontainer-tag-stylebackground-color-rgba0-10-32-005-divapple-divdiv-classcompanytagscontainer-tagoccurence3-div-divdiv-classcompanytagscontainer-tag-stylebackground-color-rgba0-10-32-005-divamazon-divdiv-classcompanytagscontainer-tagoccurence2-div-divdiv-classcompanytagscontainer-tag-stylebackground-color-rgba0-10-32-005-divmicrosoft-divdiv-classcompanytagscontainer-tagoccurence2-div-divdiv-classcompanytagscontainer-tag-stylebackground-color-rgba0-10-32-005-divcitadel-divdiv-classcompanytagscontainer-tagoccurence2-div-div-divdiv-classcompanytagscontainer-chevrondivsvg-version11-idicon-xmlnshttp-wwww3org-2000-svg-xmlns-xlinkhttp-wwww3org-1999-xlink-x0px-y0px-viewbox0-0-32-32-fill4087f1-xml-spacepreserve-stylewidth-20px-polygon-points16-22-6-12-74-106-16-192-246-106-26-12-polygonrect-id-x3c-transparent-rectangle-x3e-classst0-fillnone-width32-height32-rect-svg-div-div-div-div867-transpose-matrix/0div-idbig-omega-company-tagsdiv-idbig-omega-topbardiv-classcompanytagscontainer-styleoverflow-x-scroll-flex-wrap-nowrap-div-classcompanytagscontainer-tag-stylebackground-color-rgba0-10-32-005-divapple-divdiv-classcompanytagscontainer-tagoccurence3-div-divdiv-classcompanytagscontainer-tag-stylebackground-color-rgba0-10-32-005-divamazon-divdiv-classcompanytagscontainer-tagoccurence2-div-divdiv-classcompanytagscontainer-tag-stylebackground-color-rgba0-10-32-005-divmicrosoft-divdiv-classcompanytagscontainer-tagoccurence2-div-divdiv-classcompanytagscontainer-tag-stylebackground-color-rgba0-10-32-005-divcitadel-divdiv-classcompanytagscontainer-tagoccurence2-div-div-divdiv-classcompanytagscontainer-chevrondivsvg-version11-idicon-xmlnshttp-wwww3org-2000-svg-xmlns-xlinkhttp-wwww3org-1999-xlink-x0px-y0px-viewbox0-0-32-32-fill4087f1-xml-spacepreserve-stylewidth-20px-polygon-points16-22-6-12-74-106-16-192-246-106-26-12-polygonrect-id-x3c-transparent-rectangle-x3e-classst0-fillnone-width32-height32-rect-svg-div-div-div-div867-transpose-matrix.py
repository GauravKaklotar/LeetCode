class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        array = np.array(matrix)
        array = array.T
        return array.tolist()