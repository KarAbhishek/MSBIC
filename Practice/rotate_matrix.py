class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n//2+1):
            first = layer
            last = n-1-layer
            for idx in range(first, last):
                offset = idx - first
                tmp = matrix[first][idx]
                matrix[first][idx] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[idx][last]
                matrix[idx][last] = tmp


import numpy as np
mat = [[1,2],[3,4]]
print(np.array(mat))
Solution().rotate(mat)
print(np.array(mat))