class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dp = [[0 for w in range(len(grid[0]))] for v in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for v in range(1, len(grid)):
            for w in range(1, len(grid[0])):
                dp[v][w] = min(dp[v - 1][w], dp[v][w - 1]) + grid[v][w]
        return dp[v][w]
# def minPathSum(grid):
#     dp = [[0 for w in range(len(grid[v]))] for v in range(len(grid))]
#     for v in range(1, len(grid) + 1):
#         for w in range(1, len(grid) + 1):
#             dp[v][w] = min(dp[v-1][w], dp[v][w-1]) + grid[v-1][w-1]
#     return dp[v-1][w-1]


import numpy as np
print(np.array([[1, 2], [5, 6], [1, 1]]))
minPathSum([[1, 2], [5, 6], [1, 1]])


