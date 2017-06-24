class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix) - 1, -1, -1):
            if target == matrix[i][0]:
                return True
            elif target > matrix[i][0]:
                break
        for j in range(1, len(matrix[0])):
            if target == matrix[i][j]:
                return True
        return False